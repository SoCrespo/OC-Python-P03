#! /usr/bin/env python3
# coding: utf-8

"""
Manage the tools position in the maze.
"""

import tool
import random


class ToolManager:
    """
    Manage the tools position in the maze and player's bag.
    """

    def __init__(self, maze, player):
        self.maze = maze
        self.player = player
        self.tools = self._choose_tools_pos()

    def _choose_tools_pos(self):
        """Select 3 random positions for tools corridor."""
        tools_positions = random.sample(
            [pos for pos in self.maze.corridor.keys()
                if pos not in [self.maze.start_pos, self.maze.exit]], 3)
        return [tool.Tool(letter, pos)
                for letter, pos in zip(("e", "n", "t"), tools_positions)]

    def add_tools_in_maze(self):
        """Add letters corresponding to tools in maze dictionary"""
        for item in self.tools:
            self.maze.background[item.pos] = item.letter

    def update_player_bag(self):
        """Update player's bag content."""
        for item in self.tools:
            if self.player.pos == item.pos:
                self.player.bag.append(item)
                self.tools.remove(item)


if __name__ == "__main__":
    pass
