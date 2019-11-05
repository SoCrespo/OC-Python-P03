import pygame


class Pygameinterface:
    KEYDOWN = pygame.KEYDOWN
    ESCAPE = pygame.K_ESCAPE
    K_DOWN = pygame.K_DOWN
    K_UP = pygame.K_UP
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT

    def __init__(self):
        pass

    def open_game(self):
        pygame.init()

    def quit_game(self):
        pygame.quit()

    def event_get(self):
        pygame.event_get()
