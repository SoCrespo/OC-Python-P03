import pygame
from params import *


class Maze:

    def __init__(self, pattern):
        self.pattern = pattern
        self.background, self.height, self.width = self._import_maze()
        self.startpos, self.exit, self.corridor = self._get_positions()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(caption)
        pygame.display.set_icon(mac_img)

    # interfaces with pygame
    def open_game(self):
        pygame.init()

    def close_game(self):
        pygame.quit()

    def wait(self, duration):
        pygame.time.wait(duration)

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

    def display_layout(self):
        for i in range(self.width):
            for j in range(self.height):
                img = img_switch.get(self.background.get((i, j)))
                self.screen.blit(img, (j*img_height, i*img_width))
            pygame.display.update()

    def display_bag(self, bag):
        x = self.width * img_width
        for tool in bag:
            y = img_height * 2 * bag.index(tool)
            self.screen.blit(img_switch[tool.letter], (x, y))
            pygame.display.update()

    def display_syringe(self):
        x = self.width * img_width
        y = 6 * img_height
        self.screen.fill((0, 0, 0), (x, 0, self.width * img_width, y))
        self.screen.blit(syringe_img, (x, y))

    def display_end(self, img):
        self.screen.blit(img, (self.height / 3 * img_height,
                               self.width / 3 * img_width))
        pygame.display.update()
