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
    # Instanciate an object managing all Pygame instructions
    pgi = pygameinterface.Pygameinterface()

    while True:
        if pgi.want_to_play() is False:
            break

        # instanciate necessary objects
        laby = maze.Maze(pm.PATTERN)  # Create laby from txt pattern
        mac = hero.Hero()
        mac.pos = laby.start_pos
        game = play.Play(laby, mac)
        game.add_tools_in_maze()

        pgi.open_game()
        pgi.display_layout(laby)

        new_coord = mac.pos
        syringe = False

        action_switch = {
            "escape": pgi.quit_game,
            "up": mac.up,
            "down": mac.down,
            "left": mac.left,
            "right": mac.right,
        }
        while mac.pos != laby.exit:
            key = pgi.press_key()
            if key is None:
                continue
            else:
                new_coord = action_switch.get(key)()

            if new_coord in laby.corridor:
                laby.move_player(mac, new_coord)
                mac.update_pos(new_coord)
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
