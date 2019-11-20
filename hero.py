#! /usr/bin/env python3
# coding: utf-8

"""
Manage hero position.
"""


class Hero:
    def __init__(self):
        self.bag = []

    def up(self):
        x, y = self.pos
        return (x - 1, y)

    def down(self):
        x, y = self.pos
        return (x + 1, y)

    def left(self):
        x, y = self.pos
        return (x, y - 1)

    def right(self):
        x, y = self.pos
        return (x, y + 1)

    def update_pos(self, pos):
        self.pos = pos


if __name__ == "__main__":
    pass
