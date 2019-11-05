#! /usr/bin/env python3
# coding: utf-8

"""
Main function for Mac Gyver Game.
"""

import maze
import hero
import play
import pygameinterface
import params as pm


def main():
    """Launches MacGyver Maze game"""
    pgi = pygameinterface.Pygameinterface()
    while True:
        if pgi.want_to_play() is False:
            break
        laby = maze.Maze(pm.PATTERN)
        mac = hero.Hero()
        mac.pos = laby.start_pos
        game = play.Play(laby, mac)
        maze.tools = game.add_tools_in_maze()
        pgi.open_game()

        new_coord = mac.pos
        syringe = False

        while mac.pos != laby.exit:
            key = pgi.press_key()
            if key == "escape":
                pgi.quit_game()
            elif key == "up":
                new_coord = mac.up()
            elif key == "down":
                new_coord = mac.down()
            elif key == "left":
                new_coord = mac.left()
            elif key == "right":
                new_coord = mac.right()

            game.move_player(new_coord)
            pgi.display_layout(laby)
            game.update_player_bag()

            if not syringe:
                pgi.display_bag(mac.bag, laby)
                if len(mac.bag) == 3:
                    pgi.wait(500)
                    pgi.display_syringe(laby)
                    syringe = True

        if syringe:
            img = pm.gagne_img
        else:
            img = pm.perdu_img
        pgi.display_end(laby, img)
        pgi.wait(2000)
    pgi.quit_game()


if __name__ == "__main__":
    main()
