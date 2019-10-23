import pygame

# import du labyrinthe et des couloirs depuis pattern.txt
background_dict = {}
with open("pattern.txt", "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                for j, char in enumerate(line.strip()):
                    background_dict.update({(i,j): char})
                        
                    
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
img_switch = {
    "_": floor_img,
    "W": wall_img,
    "*": mac_img,
    ":": guard_img,
    }
for i in range(15):
    for j in range(15):
        img = img_switch.get(background_dict.get((i,j)))
        screen.blit(img,(j*40,i*40))
    pygame.display.update()    
                    
# Gestion des déplacements de MacGyver
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

move_switch = {"u" : up, "d" : down, "l": left, "r": right}
while True:
    move = input("tapez U(p), D(own), L(eft), R(ight), ou Q pour terminer :").lower()
    if move == "q": 
        break
    if move not in move_switch.keys():
        continue
    new_coord = move_switch.get(move)(mac_pos)
    if new_coord in corridor:
        mac_pos = new_coord
    print(mac_pos)
    if mac_pos == exit_pos: 
        print("Gagné !")
        break        