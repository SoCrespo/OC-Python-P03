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
    while laby.want_to_play():
        print("ca marche")
    else:
        laby.close_game()

    # End of game
    if mac.pos == laby.exit:
        if syringe:
            laby.display_end(gagne_img)
        else:
            laby.display_end(perdu_img)
        laby.wait(2000)
    
if __name__ == "__main__":
    main()
