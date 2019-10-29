import random

import pygame
import hero
import tool
from params import *
from maze import *

pygame.init()
mac = hero.Hero()
background_dict, height, width = import_maze("pattern.txt")
mac.pos, exit, corridor = get_positions(background_dict)

pos_for_tools = [pos for pos in corridor.keys() if pos not in [mac.pos, exit]]
tools_positions = random.choices(pos_for_tools, k=3)

tools = ether, needle, tube = (tool.Tool(img, pos) for img, pos in zip(
    (ether_img, needle_img, tube_img), tools_positions))

                 
# Managing MacGyver movements
new_coord = mac.pos
while mac.pos != exit:
    display_layout(background_dict, width, height)
     
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
                
    if new_coord in corridor:
        background_dict[mac.pos]= "_"
        background_dict[new_coord] = "*"    
        mac.pos = new_coord
    
    for tool in tools:
        if mac.pos == tool.pos:
            mac.bag.append(tool)
            tools.remove(tool) 
    
    #TODO : add condition to transform 3 tools into syringe                
        
    
print("Gagné !")
           
pygame.quit()         