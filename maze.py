from params import *


class Maze:

    def __init__(self, pattern):
        self.pattern = pattern
        self.background, self.height, self.width = self._import_maze()
        self.startpos, self.exit, self.corridor = self._get_positions()

    # Convert pattern.txt in maze structure
    def _import_maze(self):
        maze_from_pattern = {}
        width = 0
        height = 0
        with open(self.pattern, "r", encoding="utf8") as p:
            for i, line in enumerate(p):
                if line.strip():
                    height += 1
                for j, char in enumerate(line.strip()):
                    maze_from_pattern.update({(i, j): char})
                    if i == 1:
                        width += 1
        return maze_from_pattern, height, width

    # Extract player, exit and corridor positions in maze
    def _get_positions(self):
        startpos = []
        exit = []
        corridor = {}
        for coord, char in self.background.items():
            if char == "*":
                startpos.append(coord)
            elif char in (":", "_"):
                corridor.update({coord: char})
                if char == ":":
                    exit.append(coord)
        if not (len(startpos) == len(exit) == 1):
            raise ValueError("Erreur sur position de MacGyver ou de la sortie")
        else:
            return startpos[0], exit[0], corridor

    # Set game window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(caption)
    pygame.display.set_icon(mac_img)

    def display_layout(maze_dict, width, height):
        for i in range(self.width):
            for j in range(self.startheight):
                img = img_switch.get(self.background.get((i, j)))
                screen.blit(img, (j*img_height, i*img_width))
            pygame.display.update()

    def display_bag(bag):
        width, height = screen_size
        x = width - img_width
        for tool in bag:
            y = img_height * 2 * bag.index(tool)
            screen.blit(img_switch[tool.letter], (x, y))
            pygame.display.update()

    def make_syringe():
        width, height = screen_size
        x = width - img_width
        y = 6 * img_height
        screen.fill((0, 0, 0), (x, 0, width, y))
        screen.blit(syringe_img, (x, y))

    def display_end(img):
        width, height = screen_size
        screen.blit(img, (height/3, width/3))
        pygame.display.update()
