import pygame

screen_size = 800, 800
img_height = 40
img_width = 40

floor_img = pygame.image.load("./resources/floor.png")
wall_img = pygame.image.load("./resources/wall.png")
mac_img = pygame.image.load("./resources/macgyver.png")
guard_img = pygame.image.load("./resources/guard.png")
needle_img = pygame.image.load("./resources/needle.png")
tube_img = pygame.image.load("./resources/tube.png")
ether_img = pygame.image.load("./resources/ether.png")

img_switch = {
    "_": floor_img,
    "W": wall_img,
    "*": mac_img,
    ":": guard_img,
    }
caption = "Labyrinthe Mac Gyver"