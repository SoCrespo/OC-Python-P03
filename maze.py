from params import *
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