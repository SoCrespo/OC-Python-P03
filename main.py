#! /usr/bin/env python3
# coding: utf-8

import maze
import hero
import params as pm


def main():
    """Launches MacGyver Maze game"""
    # Instantiate game and MacGyver
    laby = maze.Maze(pm.PATTERN)
    mac = hero.Hero()
    mac.pos = laby.startpos
    laby.open_game()
    
    # Wait for the player to press ENTER to play or ESC to exit
    if(laby.want_to_play()): 
        print("ca marche")
    else:
        laby.close_game()    
    
    
    
    
if __name__ == "__main__":
    main()    