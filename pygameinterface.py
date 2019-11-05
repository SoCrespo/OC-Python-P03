import pygame


class Pygameinterface:
    """ Constants and functions imported from pygame."""
    KEYDOWN = pygame.KEYDOWN
    ESCAPE = pygame.K_ESCAPE
    K_DOWN = pygame.K_DOWN
    K_UP = pygame.K_UP
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT

    def __init__(self):
        pass

    def open_game(self):
        """ return pygame.init"""
        pygame.init()

    def quit_game(self):
        """Return pygame.quit"""
        pygame.quit()

    def event_get(self):
        """Return pygame.event_get."""
        pygame.event_get()
