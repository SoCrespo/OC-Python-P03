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

- the maze must be entirely closed with walls, except for one, and only one, exit.
- DO NOT locate the exit in a corner, since MacGyver cannot move diagonally.

Here is an example of how to represent a small structure of 4 x  cells, the exit is in the east wall
(depending on the font, the maze may seem to be not square-shaped):  

WWWW  
W*_:  
WWWW
"""

import random

import maze
import hero
import item


the_maze = maze.Maze("pattern.txt")

mac_gyver = hero.Hero("MacGyver")
guard = item.Item("Guard")
needle = item.Item("Needle")
tube = item.Item("Tube")
ether = item.Item("Ether")

tools_positions = random.choices(list(the_maze.corridor.keys()), k=3)

positions = {
    mac_gyver : the_maze.mac_pos, 
    guard :     the_maze.exit_pos, 
    needle :    tools_positions[0],
    tube :      tools_positions[1],
    ether :     tools_positions[2], 
    }

def get_position(player)
    return x, y = positions.get(player)

def try_up(player):
    new_position = (x, y - 1)
        
def try_down(player):
    new_position = (x, y + 1) 
    
def try_left(player):
    new_position = (x - 1, y)            
    
def try_right(player):
    new_position = (x + 1 , y)      
               
def move(new_pos):
    if pos in the_maze.corridor:
        positions[player] = new_pos

def pick_tool(player):
    
    pass

def syringe():
# return boolean
    pass

def try_exit():
    pass
           