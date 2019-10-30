from params import *


# Convert pattern.txt in maze structure
def import_maze(pattern):
    maze_from_pattern = {}
    width = 0
    height = 0
    with open(pattern, "r", encoding="utf8") as p:
        for i, line in enumerate(p):
            if line.strip():
                height += 1
            for j, char in enumerate(line.strip()):
                maze_from_pattern.update({(i, j): char})
                if i == 1:
                    width += 1
    return maze_from_pattern, height, width


# Extract player, exit and corridor positions in maze
def get_positions(structure_dict):
    player_pos = []
    exit_pos = []
    corridor = {}
    for coord, char in structure_dict.items():
        if char == "*":
            player_pos.append(coord)
        elif char in (":", "_"):
            corridor.update({coord: char})
            if char == ":":
                exit_pos.append(coord)
    if not (len(player_pos) == len(exit_pos) == 1):
        raise ValueError("Erreur sur position de MacGyver ou de la sortie")
    else:
        return player_pos[0], exit_pos[0], corridor


# Set game window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(caption)
pygame.display.set_icon(mac_img)


# Display layout
def display_layout(maze_dict, width, height):
    for i in range(width):
        for j in range(height):
            img = img_switch.get(maze_dict.get((i, j)))
            screen.blit(img, (j*img_height, i*img_width))
        pygame.display.update()


def display_end(img):
    width, height = screen_size
    screen.blit(img, (height/3, width/3))
    pygame.display.update()
