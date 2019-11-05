#! /usr/bin/env python3
# coding: utf-8

"""Manages the logic of the game.
Calculate random position of tools,
manages player moves and their consequences.
"""

import random
import tool
import params
import pygameinterface as py


class Play:
    def __init__(self, maze, player):
        self.maze = maze
        self.player = player
        self.tools = self.set_tools_positions()



    def display_game(self):
        """Display game deck at its inital position."""
        self.maze.display_layout()

    def move_player(self):
        new_coord = self.player.pos
        syringe = False

        while self.player.pos != self.maze.exit:

            # Get the pressed key
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        py.quit()
                    elif event.key == py.K_DOWN:
                        new_coord = self.player.down()
                    elif event.key == py.K_UP:
                        new_coord = self.player.up()
                    elif event.key == py.K_LEFT:
                        new_coord = self.player.left()
                    elif event.key == py.K_RIGHT:
                        new_coord = self.player.right()

            # Update and display player position
            if new_coord in self.maze.corridor:
                self.maze.background[self.player.pos] = "_"
                self.maze.background[new_coord] = "*"
                self.player.pos = new_coord
                self.maze.display_layout()

            # Update player's bag content
            for item in self.tools:
                if self.player.pos == item.pos:
                    self.player.bag.append(item)
                    self.tools.remove(item)
                    self.maze.display_bag(self.player.bag)

            # Transform 3 tools into syringe
            if len(self.player.bag) == 3 and not syringe:
                self.maze.wait(500)
                self.maze.display_syringe()
                syringe = True

            # End of game
            if self.player.pos == self.maze.exit:
                if syringe:
                    self.maze.display_end(params.gagne_img)
                else:
                    self.maze.display_end(params.perdu_img)
                self.maze.wait(2000)
