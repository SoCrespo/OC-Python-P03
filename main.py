#! /usr/bin/env python3
# coding: utf-8

import maze
import hero
import game
import pygameinterface
import params as pm


def main():
    """Launches MacGyver Maze game"""
    pgi = pygameinterface.Pygameinterface()
    while True:
        laby = maze.Maze(pm.PATTERN)
        play = laby.want_to_play()
        if play is False:
            break
        mac = hero.Hero()
        mac.pos = laby.startpos
        pgi.open_game()
        game.play(laby, mac)
    pgi.quit_game()


if __name__ == "__main__":
    main()
