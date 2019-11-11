#! /usr/bin/env python3
# coding: utf-8

"""
Interfacing with pygame. Manages all displays.
"""

import pygame
import params as pm


class Pygameinterface:
    """
    Interfacing with pygame. Manages all displays.
    """

    def __init__(self):

        self.floor_img = pygame.image.load(pm.FLOOR_IMG_PATH)
        self.wall_img = pygame.image.load(pm.WALL_IMG_PATH)
        self.mac_img = pygame.image.load(pm.MAC_IMG_PATH)
        self.guard_img = pygame.image.load(pm.GUARD_IMG_PATH)
        self.needle_img = pygame.image.load(pm.NEEDLE_IMG_MATH)
        self.tube_img = pygame.image.load(pm.TUBE_IMG_PATH)
        self.ether_img = pygame.image.load(pm.ETHER_IMG_PATH)
        self.syringe_img = pygame.image.load(pm.SYRINGE_IMG_PATH)
        self.gagne_img = pygame.image.load(pm.GAGNE_IMG_PATH)
        self.perdu_img = pygame.image.load(pm.PERDU_IMG_PATH)
        self.menu_img = pygame.image.load(pm.MENU_IMG_PATH)
        self.caption = pm.CAPTION

        self.img_switch = {
            "_": self.floor_img,
            "W": self.wall_img,
            "*": self.mac_img,
            ":": self.guard_img,
            "e": self.ether_img,
            "n": self.needle_img,
            "t": self.tube_img,
            }

        self.screen = pygame.display.set_mode(pm.SCREEN_SIZE)
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(self.mac_img)

    def open_game(self):
        """ return pygame.init"""
        pygame.init()

    def quit_game(self):
        """Return pygame.quit"""
        pygame.quit()

    def wait(self, duration):
        """Return pygame.type.wait."""
        pygame.time.wait(duration)

    def event_get(self):
        """Return pygame.event_get."""
        pygame.event_get()

    def show_start_menu(self):
        """
        Display a message to ask player for playing or exit.
        """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.menu_img, (0, 50))
        pygame.display.update()

    def want_to_play(self):
        '''Return True if player presses Enter, False if presses ESC.'''
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        self.screen.fill((0, 0, 0))
                        pygame.display.update()
                        return True

    def display_layout(self, maze):
        """Display game board based on Maze.background."""
        for i in range(maze.width):
            for j in range(maze.height):
                img = self.img_switch.get(maze.background.get((i, j)))
                self.screen.blit(img,
                                 (j*pm.IMG_HEIGHT, i*pm.IMG_WIDTH))
            pygame.display.flip()

    def display_bag(self, bag, maze):
        """Display player's bag content on maze side."""
        x = maze.width * pm.IMG_WIDTH
        for tool in bag:
            y = pm.IMG_HEIGHT * 2 * bag.index(tool)
            self.screen.blit(self.img_switch[tool.letter], (x, y))
            pygame.display.update()

    def display_syringe(self, maze):
        """Erase picked up tools and display the syringe."""
        x = maze.width * pm.IMG_WIDTH
        y = 6 * pm.IMG_HEIGHT
        self.screen.fill((0, 0, 0), (x, 0, x, y))
        pygame.display.update()
        self.screen.blit(self.syringe_img, (x, y))
        pygame.display.update()

    def display_end(self, maze, win):
        """Display the result of the game."""
        if win is True:
            img = self.gagne_img
        else:
            img = self.perdu_img
        self.screen.blit(img, (maze.height / 5 * pm.IMG_HEIGHT,
                               maze.width / 5 * pm.IMG_WIDTH))
        pygame.display.update()

    def press_key(self):
        """
        Get the pressed key and return a string
        'escape', 'up', 'down', 'left' or 'right'.
        """
        keys_switch = {
            pygame.K_ESCAPE: "escape",
            pygame.K_DOWN: "down",
            pygame.K_UP: "up",
            pygame.K_LEFT: "left",
            pygame.K_RIGHT: "right"
        }
        event = pygame.event.wait()
        while event.type != pygame.KEYDOWN:
            event = pygame.event.wait()
        return keys_switch.get(event.key)


if __name__ == "__main__":
    pass
