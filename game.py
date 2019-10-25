import pygame

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
screen_size = 800, 800

floor_img = pygame.image.load("./resources/floor.png")
wall_img = pygame.image.load("./resources/wall.png")
mac_img = pygame.image.load("./resources/macgyver.png")
guard_img = pygame.image.load("./resources/guard.png")
    
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Labyrinthe Mac Gyver")
pygame.display.set_icon(mac_img)
img_switch = {
    "_": floor_img,
    "W": wall_img,
    "*": mac_img,
    ":": guard_img,
    }
def update_layout():
    for i in range(width):
        for j in range(height):
            img = img_switch.get(background_dict.get((i,j)))
            screen.blit(img,(j*40,i*40))
        pygame.display.update()

update_layout()
                 
# Définition des déplacements de MacGyver

def up(coord):
    x, y = coord
    return (x - 1, y)

def down(coord):
    x, y = coord
    return (x + 1, y)    

def left(coord):
    x, y = coord
    return (x, y - 1)

def right(coord):
    x, y = coord
    return (x, y + 1)


# Gestion des mouvements
new_coord = mac_pos
while mac_pos != exit_pos:
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                new_coord = down(mac_pos) 
            elif event.key == pygame.K_UP:
                new_coord = up(mac_pos) 
            elif event.key == pygame.K_LEFT:
                new_coord = left(mac_pos) 
            elif event.key == pygame.K_RIGHT:
                new_coord = right(mac_pos) 
            
    if new_coord in corridor:
        background_dict[mac_pos]= "_"
        background_dict[new_coord] = "*"    
        mac_pos = new_coord
    
    for i in range(width):
        for j in range(height):
            img = img_switch.get(background_dict.get((i,j)))
            screen.blit(img,(j*40,i*40))
        pygame.display.update()    
           
    
print("Gagné !")
           
pygame.quit()         