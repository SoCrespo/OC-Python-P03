#! /usr/bin/env python3
# coding: utf-8

import maze
import hero
import game
import params as pm


def main():
    """Launches MacGyver Maze game"""
    while True :
        laby = maze.Maze(pm.PATTERN)
        play = laby.want_to_play()
        if play == False :
            break
        mac = hero.Hero()
        mac.pos = laby.startpos
        laby.open_game()
        game.play(laby, mac)
    laby.close_game()


if __name__ == "__main__":
    main()
