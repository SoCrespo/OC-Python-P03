import pygame
import hero
from params import *
from maze import *

pygame.init()
mac = hero.Hero()
        
# Extracting player, exit and corridor positions in maze
player_pos = []
exit_pos = []
corridor = {}
for coord, char in background_dict.items():
    if char == "*":
        player_pos.append(coord)
    elif char in (":", "_"):
        corridor.update({coord: char}) 
        if char == ":":
            exit_pos.append(coord)     
if not (len(player_pos) == len(exit_pos) == 1) :
    raise ValueError("Erreur sur position de MacGyver ou de la sortie")
else:
    mac.pos = player_pos[0]
    exit_pos = exit_pos[0]

                 
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