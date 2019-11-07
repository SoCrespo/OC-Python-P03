#! /usr/bin/env python3
# coding: utf-8

"""
This file contains relative paths to files used in the game.

All the images are located in the ./resources directory. If you want to
change them, e.g. replace the guard's image, please do as follow :
- use a png file
- the image must be the same size as the one it replaces
- rename the file to keep the path intact.

The maze pattern is in the pattern.txt file and can be modified.
it must have a square or rectangular structure.
Each cell is represented by a specific character:
" W " (uppercase) for a piece of wall
" _ " (key 8 of the keyboard) for a piece of corridor
" * " for the initial position of MacGyver
" : " for the exit (position of the guard).

*Please note:*

- the maze must be entirely closed with walls, except for one,
and only one, exit.
- DO NOT locate the exit in a corner, since MacGyver cannot move diagonally.

Here is an example of how to represent a small structure of 4 x  cells
the exit is in the east wall
(depending on the font, the maze may seem to be not square-shaped):

WWWW
W*_:
WWWW


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
