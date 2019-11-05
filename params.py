#! /usr/bin/env python3
# coding: utf-8

"""
Parameters for Mac Gyver Game.
"""


import pygame

PATTERN = "pattern.txt"

SCREEN_SIZE = 640, 600
IMG_HEIGHT = 40
IMG_WIDTH = 40

floor_img = pygame.image.load("./resources/floor.png")
wall_img = pygame.image.load("./resources/wall.png")
mac_img = pygame.image.load("./resources/macgyver.png")
guard_img = pygame.image.load("./resources/guard.png")
needle_img = pygame.image.load("./resources/needle.png")
tube_img = pygame.image.load("./resources/tube.png")
ether_img = pygame.image.load("./resources/ether.png")
syringe_img = pygame.image.load("./resources/syringe.png")
gagne_img = pygame.image.load("./resources/gagne.png")
perdu_img = pygame.image.load("./resources/perdu.png")
menu_img = pygame.image.load("./resources/menu.png")

img_switch = {
    "_": floor_img,
    "W": wall_img,
    "*": mac_img,
    ":": guard_img,
    "e": ether_img,
    "n": needle_img,
    "t": tube_img
    }
caption = "Labyrinthe Mac Gyver"

if __name__ == "__main__":
    pass
