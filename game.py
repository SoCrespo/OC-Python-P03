import random

import pygame
import hero
import tool
from params import *
from maze import *

# Instantiate game and MacGyver
pygame.init()
mac = hero.Hero()
background_dict, height, width = import_maze("pattern.txt")
mac.pos, exit, corridor = get_positions(background_dict)


# Select 3 random positions for tools in corridor
tools_positions = random.sample([pos for pos in corridor.keys()
                                if pos not in [mac.pos, exit]], 3)
tools = ether, needle, tube = [tool.Tool(letter, pos) for letter, pos in
                               zip(("e", "n", "t"), tools_positions)]
for tool in tools:
    background_dict[tool.pos] = tool.letter


new_coord = mac.pos
display_layout(background_dict, width, height)

# Manage MacGyver movements
while mac.pos != exit:

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
    if new_coord in corridor:
        background_dict[mac.pos] = "_"
        background_dict[new_coord] = "*"
        mac.pos = new_coord
        display_layout(background_dict, width, height)

    # Update player's bag content
    for tool in tools:
        if mac.pos == tool.pos:
            mac.bag.append(tool)
            tools.remove(tool)

# End of game
    if mac.pos == exit:
        if tools == []:
            display_end(gagne_img)
        else:
            display_end(perdu_img)

pygame.time.wait(2000)
pygame.quit()
