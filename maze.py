#! /usr/bin/env python3
# coding: utf-8

"""Manage the game board displaying."""
import pygame
from params import *


class Maze:
    """Display the game board."""

    def __init__(self, pattern):
        """Create the maze based on pattern.txt."""
        self.pattern = pattern
        self.background, self.height, self.width = self._import_maze()
        self.startpos, self.exit, self.corridor = self._get_positions()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(caption)
        pygame.display.set_icon(mac_img)

    def open_game(self):
        """Return pygame.init."""
        pygame.init

    def close_game(self):
        """Return pygame.quit."""
        pygame.quit

    def wait(self, duration):
        """Return pygame.type.wait."""
        pygame.time.wait(duration)

    def _import_maze(self):
        """
        Convert txt pattern into dictionary.

        Return a tuple with:
        - this dictionary,
        - heigth (number of lines)
        - width (number of characters)
        of the pattern.
        """
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

    def _get_positions(self):
        """
        Extract informations from maze dictionary.

        Return a tuple with macGyver start position (tuple),
        exit position (tuple)
        dictionary of the corridors cells

        """
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
        """Display game board."""
        for i in range(self.width):
            for j in range(self.height):
                img = img_switch.get(self.background.get((i, j)))
                self.screen.blit(img, (j*IMG_HEIGHT, i*IMG_WIDTH))
            pygame.display.update()

    def display_bag(self, bag):
        """Display mac's bag content on the maze side."""
        x = self.width * IMG_WIDTH
        for tool in bag:
            y = IMG_HEIGHT * 2 * bag.index(tool)
            self.screen.blit(img_switch[tool.letter], (x, y))
            pygame.display.update()

    def display_syringe(self):
        """Erase picked up tools and display the syringe."""
        x = self.width * IMG_WIDTH
        y = 6 * IMG_HEIGHT
        self.screen.fill((0, 0, 0), (x, 0, self.width * IMG_WIDTH, y))
        self.screen.blit(syringe_img, (x, y))

    def display_end(self, img):
        """Display the result of the game."""
        self.screen.blit(img, (self.height / 5 * IMG_HEIGHT,
                               self.width / 5 * IMG_WIDTH))
        pygame.display.update()


if __name__ == "__main__":
    pass
