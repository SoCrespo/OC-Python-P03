import pygame
import hero
from params import *
from maze import *

pygame.init()
mac = hero.Hero()
        
mac.pos, exit_pos, corridor = get_positions()

                 
# Managing MacGyver movements
new_coord = mac.pos
while mac.pos != exit_pos:
    display_layout() 
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
    
print("Gagné !")
           
pygame.quit()         