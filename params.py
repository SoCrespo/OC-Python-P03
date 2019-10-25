import pygame

screen_size = 800, 800
img_height = 40
img_width = 40

floor_img = pygame.image.load("./resources/floor.png")
wall_img = pygame.image.load("./resources/wall.png")
mac_img = pygame.image.load("./resources/macgyver.png")
guard_img = pygame.image.load("./resources/guard.png")

img_switch = {
    "_": floor_img,
    "W": wall_img,
    "*": mac_img,
    ":": guard_img,
    }
caption = "Labyrinthe Mac Gyver"
screen = pygame.display.set_mode(screen_size)