import pygame
import hero
from params import *
from maze import *

pygame.init()
mac = hero.Hero()
        
# extraction du couloir, des positions de MG de de la sortie
mac_pos = []
exit_pos = []
corridor = {}
for coord, char in background_dict.items():
    if char == "*":
        mac_pos.append(coord)
    elif char in (":", "_"):
        corridor.update({coord: char}) 
        if char == ":":
            exit_pos.append(coord)     
if not (len(mac_pos) == len(exit_pos) == 1) :
    raise ValueError("Erreur sur position de MacGyver ou de la sortie")
else:
    mac_pos = mac_pos[0]
    exit_pos = exit_pos[0]

                 
# Gestion des mouvements
new_coord = mac_pos
while mac_pos != exit_pos:
    display_layout()
    
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                new_coord = mac.down(mac_pos) 
            elif event.key == pygame.K_UP:
                new_coord = mac.up(mac_pos) 
            elif event.key == pygame.K_LEFT:
                new_coord = mac.left(mac_pos) 
            elif event.key == pygame.K_RIGHT:
                new_coord = mac.right(mac_pos) 
            
    if new_coord in corridor:
        background_dict[mac_pos]= "_"
        background_dict[new_coord] = "*"    
        mac_pos = new_coord
    
print("Gagné !")
           
pygame.quit()         