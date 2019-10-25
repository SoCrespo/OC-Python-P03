import pygame
import hero
from params import *

mac = hero.Hero()

# import du labyrinthe et des couloirs depuis pattern.txt

background_dict = {}
width = 0
height = 0
with open("pattern.txt", "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                if line.strip():
                    height += 1
                for j, char in enumerate(line.strip()):
                    background_dict.update({(i,j): char})
                    if i == 1 : 
                        width += 1                      
                    
def update_layout():
    for i in range(width):
        for j in range(height):
            img = img_switch.get(background_dict.get((i,j)))
            screen.blit(img,(j*img_height,i*img_width))
        pygame.display.update()
        
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

# Affichage du labyrinthe
pygame.init()
    
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Labyrinthe Mac Gyver")
pygame.display.set_icon(mac_img)


update_layout()
                 
# Gestion des mouvements
new_coord = mac_pos
while mac_pos != exit_pos:
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
    
    update_layout()
    
           
    
print("Gagné !")
           
pygame.quit()         