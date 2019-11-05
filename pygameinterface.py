#! /usr/bin/env python3
# coding: utf-8

"""
Interfacing with pygame.
Manages all displays.
"""

import pygame
import params


class Pygameinterface:
    """ Functions imported from pygame."""

    def __init__(self):
        self.screen = pygame.display.set_mode(params.SCREEN_SIZE)
        pygame.display.set_caption(params.caption)
        pygame.display.set_icon(params.mac_img)

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

    def want_to_play(self):
        """
        Display a message to ask player for playing or exit.
        Return True if player press Enter,
        False if player press ESC.
        """
        self.screen.fill((0, 0, 0))
        self.screen.blit(params.menu_img, (0, 50))
        pygame.display.update()
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
        """Display game board."""
        for i in range(maze.width):
            for j in range(maze.height):
                img = params.img_switch.get(maze.background.get((i, j)))
                self.screen.blit(img,
                                 (j*params.IMG_HEIGHT, i*params.IMG_WIDTH))
            pygame.display.flip()

    def display_bag(self, bag, maze):
        """Display mac's bag content on maze side."""
        x = maze.width * params.IMG_WIDTH
        for tool in bag:
            y = params.IMG_HEIGHT * 2 * bag.index(tool)
            self.screen.blit(params.img_switch[tool.letter], (x, y))
            pygame.display.update()

    def display_syringe(self, maze):
        """Erase picked up tools and display the syringe."""
        x = maze.width * params.IMG_WIDTH
        y = 6 * params.IMG_HEIGHT
        self.screen.fill((0, 0, 0), (x, 0, x, y))
        pygame.display.update()
        self.screen.blit(params.syringe_img, (x, y))
        pygame.display.update()

    def display_end(self, maze, img):
        """Display the result of the game."""
        self.screen.blit(img, (maze.height / 5 * params.IMG_HEIGHT,
                               maze.width / 5 * params.IMG_WIDTH))
        pygame.display.update()

    def press_key(self):
        """
        Get the pressed key and return a string
        'escape', 'up', 'down', 'left' or 'right'.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "escape"
                elif event.key == pygame.K_DOWN:
                    return "down"
                elif event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_LEFT:
                    return "left"
                elif event.key == pygame.K_RIGHT:
                    return "right"


if __name__ == "__main__":
    pass
