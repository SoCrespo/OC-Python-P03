#! /usr/bin/env python3
# coding: utf-8

"""
This file contains constants and relative paths to images used in the game.
"""


""" PLEASE DO NOT CHANGE THE 3 FOLLOWING CONSTANTS """
SCREEN_SIZE = 640, 600  # Size of game screen

IMG_HEIGHT = 40  # Height in px of all images used in the maze:
#                  walls, corridor, guard, hero, tools

IMG_WIDTH = 40  # Width in px of all images used in the maze:
#                  walls, corridor, guard, hero, tools

"""
The maze pattern is in the pattern.txt file (same folder as the present file).
This pattern can be modified.
it must have a square or rectangular structure.
Each cell is represented by a specific character:
" W " (uppercase) for a piece of wall
" _ " (key 8 of the keyboard) for a piece of corridor
" * " for the initial position of MacGyver
" : " for the exit (position of the guard).

*Please note:*
- use only the specified characters
- the maze must be entirely closed with walls, except for one,
and only one, exit.
- DO NOT locate the exit in a corner, since MacGyver cannot move diagonally.

Here is an example of how to represent a small structure of 4 x 4 cells,
exit in the east wall:

WWWW
W*_:
WWWW
"""

PATTERN = "pattern.txt"


"""
All the images are located in ./resources directory. If you want to
change an image, please only use a PNG file exactly the same size
than indicated.
"""

FLOOR_IMG_PATH = "./resources/floor.png"  # size IMG_WIDTH x IMG_HEIGHT px
WALL_IMG_PATH = "./resources/wall.png"  # size IMG_WIDTH x IMG_HEIGHT px
MAC_IMG_PATH = "./resources/macgyver.png"  # size IMG_WIDTH x IMG_HEIGHT px
GUARD_IMG_PATH = "./resources/guard.png"  # size IMG_WIDTH x IMG_HEIGHT px
NEEDLE_IMG_MATH = "./resources/needle.png"  # size IMG_WIDTH x IMG_HEIGHT px
TUBE_IMG_PATH = "./resources/tube.png"  # size IMG_WIDTH x IMG_HEIGHT px
ETHER_IMG_PATH = "./resources/ether.png"  # size IMG_WIDTH x IMG_HEIGHT px
SYRINGE_IMG_PATH = "./resources/syringe.png"  # size IMG_WIDTH x IMG_HEIGHT px
GAGNE_IMG_PATH = "./resources/gagne.png"  # max 500 x 150 px
PERDU_IMG_PATH = "./resources/perdu.png"  # max 500 x 150 px
MENU_IMG_PATH = "./resources/menu.png"  # same size as SCREEN_SIZE

CAPTION = "Labyrinthe Mac Gyver"  # Max 30 char
