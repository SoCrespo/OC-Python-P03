#! /usr/bin/env python3
# coding: utf-8

"""Manages the logic of the game.
Calculate random position of tools,
manages player moves and their consequences.
"""

import random
import tool
import pygame as py
import params


def play(maze, player):

    # Select 3 random positions for tools in maze.corridor
    tools_positions = random.sample([pos for pos in maze.corridor.keys()
                                    if pos not in [player.pos, maze.exit]], 3)
    tools = [tool.Tool(letter, pos) for letter, pos in
             zip(("e", "n", "t"), tools_positions)]

    # Assign tools positions in game dictionary
    for item in tools:
        maze.background[item.pos] = item.letter

    # Display game deck at its inital position
    maze.display_layout()

    # Manage MacGyver movements
    new_coord = player.pos
    syringe = False

    while player.pos != maze.exit:

        # Get the pressed key
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()
                elif event.key == py.K_DOWN:
                    new_coord = player.down()
                elif event.key == py.K_UP:
                    new_coord = player.up()
                elif event.key == py.K_LEFT:
                    new_coord = player.left()
                elif event.key == py.K_RIGHT:
                    new_coord = player.right()

        # Update and display player position
        if new_coord in maze.corridor:
            maze.background[player.pos] = "_"
            maze.background[new_coord] = "*"
            player.pos = new_coord
            maze.display_layout()

        # Update player's bag content
        for item in tools:
            if player.pos == item.pos:
                player.bag.append(item)
                tools.remove(item)
                maze.display_bag(player.bag)

        # Transform 3 tools into syringe
        if len(player.bag) == 3 and not syringe:
            maze.wait(500)
            maze.display_syringe()
            syringe = True

        # End of game
        if player.pos == maze.exit:
            if syringe:
                maze.display_end(params.gagne_img)
            else:
                maze.display_end(params.perdu_img)
            maze.wait(2000)
