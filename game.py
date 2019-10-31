#! /usr/bin/env python3
# coding: utf-8

import random

import pygame
import hero
import tool
import maze
from params import *


# Instantiate game and MacGyver
laby = maze.Maze(PATTERN)
mac = hero.Hero()
mac.pos = laby.startpos
laby.open_game()


# Select 3 random positions for tools in laby.corridor
tools_positions = random.sample([pos for pos in laby.corridor.keys()
                                if pos not in [mac.pos, laby.exit]], 3)
tools = ether, needle, tube = [tool.Tool(letter, pos) for letter, pos in
                               zip(("e", "n", "t"), tools_positions)]

# Assign tools positions in game dictionary
for tool in tools:
    laby.background[tool.pos] = tool.letter

# Display game deck at its inital position
laby.display_layout()

# Manage MacGyver movements
new_coord = mac.pos
syringe = False

while mac.pos != laby.exit:

    # Get the pressed key
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_DOWN:
                new_coord = mac.down()
            elif event.key == pygame.K_UP:
                new_coord = mac.up()
            elif event.key == pygame.K_LEFT:
                new_coord = mac.left()
            elif event.key == pygame.K_RIGHT:
                new_coord = mac.right()

    # Update and display player position
    if new_coord in laby.corridor:
        laby.background[mac.pos] = "_"
        laby.background[new_coord] = "*"
        mac.pos = new_coord
        laby.display_layout()

    # Update player's bag content
    for tool in tools:
        if mac.pos == tool.pos:
            mac.bag.append(tool)
            tools.remove(tool)
            laby.display_bag(mac.bag)

    # Transform 3 tools into syringe
    if tools == [] and not syringe:
        laby.wait(500)
        laby.display_syringe()
        syringe = True

    # End of game
    if mac.pos == laby.exit:
        if syringe:
            laby.display_end(gagne_img)
        else:
            laby.display_end(perdu_img)

laby.wait(2000)
laby.close_game()
