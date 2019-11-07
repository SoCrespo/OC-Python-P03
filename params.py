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

PATTERN = "pattern.txt"

SCREEN_SIZE = 640, 600
IMG_HEIGHT = 40
IMG_WIDTH = 40

FLOOR_IMG_PATH = "./resources/floor.png"
WALL_IMG_PATH = "./resources/wall.png"
MAC_IMG_PATH = "./resources/macgyver.png"
GUARD_IMG_PATH = "./resources/guard.png"
NEEDLE_IMG_MATH = "./resources/needle.png"
TUBE_IMG_PATH = "./resources/tube.png"
ETHER_IMG_PATH = "./resources/ether.png"
SYRINGE_IMG_PATH = "./resources/syringe.png"
GAGNE_IMG_PATH = "./resources/gagne.png"
PERDU_IMG_PATH = "./resources/perdu.png"
MENU_IMG_PATH = "./resources/menu.png"

CAPTION = "Labyrinthe Mac Gyver"
