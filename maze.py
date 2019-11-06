#! /usr/bin/env python3
# coding: utf-8

"""Manage the game board structure."""


class Maze:
    """Manage the game board structure."""

    def __init__(self, pattern):
        """Create the maze based on txt pattern."""
        self.pattern = pattern
        self.background, self.height, self.width = self._import_maze()
        self.start_pos, self.exit, self.corridor = self._get_positions()

    def _import_maze(self):
        """
        Convert txt pattern into dictionary.

        Return a tuple with:
        - this dictionary,
        - height (number of lines)
        - width (number of characters)
        of the pattern.
        """
        maze_from_pattern = {}
        width = 0
        height = 0
        with open(self.pattern, "r", encoding="utf8") as p:
            for i, line in enumerate(p):
                if line.strip():
                    height += 1
                for j, char in enumerate(line.strip()):
                    maze_from_pattern.update({(i, j): char})
                    if i == 1:
                        width += 1
        return maze_from_pattern, height, width

    def _get_positions(self):
        """
        Extract informations from maze dictionary.

        Return a tuple with macGyver start position (tuple),
        exit position (tuple)
        dictionary of the corridors cells

        """
        start_pos = []
        exit = []
        corridor = {}
        for coord, char in self.background.items():
            if char == "*":
                start_pos.append(coord)
            elif char in (":", "_"):
                corridor.update({coord: char})
                if char == ":":
                    exit.append(coord)
        if not (len(start_pos) == len(exit) == 1):
            raise ValueError("Erreur sur position de MacGyver ou de la sortie")
        else:
            return start_pos[0], exit[0], corridor

    def move_player(self, player, coord):
        """Move player to new position in maze."""
        self.background[player.pos] = "_"
        self.background[coord] = "*"


if __name__ == "__main__":
    pass
