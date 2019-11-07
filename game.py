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


class Game:
    """Manages MacGyver Maze game"""

    def __init__(self):
        self.pgi = pygameinterface.Pygameinterface()  # Create Pygame interface
        self.laby = maze.Maze(pm.PATTERN)  # Create laby from txt pattern
        self.mac = hero.Hero()  # Create player
        self.mac.pos = self.laby.start_pos  # Set player starting position
        #                                     according to pattern
        self.game = play.Play(self.laby, self.mac)  # Create object managing
        #                                             tools positions
        self.syringe = False  # Player has no syringe at beginning

    def show_start_menu(self):
        '''Display a message to ask player for playing or exit.'''
        self.pgi.show_start_menu()

    def want_to_play(self):
        '''
        Return True if Enter is pressed,
        False if presses ESC.
        '''
        return self.pgi.want_to_play()

    def add_tools_in_maze(self):
        '''
        Add letter corresponding to each tool in maze.background.
        '''
        self.game.add_tools_in_maze()

    def display_graphic_layer(self):
        '''
        Start pygame interface and display the game deck.
        '''
        self.pgi.open_game()
        self.pgi.display_layout(self.laby)

    def calc_move(self):
        ''' Calculates player new coordinates according to pressed key'''
        action_switch = {
            "escape": self.pgi.quit_game,
            "up": self.mac.up,
            "down": self.mac.down,
            "left": self.mac.left,
            "right": self.mac.right,
        }
        while self.mac.pos != self.laby.exit:
            key = self.pgi.press_key()
            if key is None:
                continue
            else:
                return action_switch.get(key)()

    def confirm_move(self, coord):
        '''Move player logically and graphically,
        and pick up tool if there is.'''
        if coord in self.laby.corridor:
            self.laby.move_player(self.mac, coord)
            self.mac.update_pos(coord)
            self.pgi.display_layout(self.laby)
            self.game.update_player_bag()

    def make_syringe(self):
        '''Make syringe when 3 tools are in player's bag.'''
        if not self.syringe:
            self.pgi.display_bag(self.mac.bag, self.laby)
            if len(self.mac.bag) == 3:
                self.pgi.wait(500)
                self.pgi.display_syringe(self.laby)
                self.syringe = True

    def exit_reached(self):
        return self.mac.pos == self.laby.exit

    def escape(self):
        '''Test if player has syringe and display win or lose.'''
        if self.syringe:
            win = True
        else:
            win = False
        self.pgi.display_end(self.laby, win)
        self.pgi.wait(2000)

    def end_game(self):
        '''Exit game.'''
        self.pgi.quit_game()


def main():
    while True:
        g = Game()
        g.show_start_menu()
        if not g.want_to_play():
            break
        while not g.exit_reached():
            g.add_tools_in_maze()
            g.display_graphic_layer()
            new_pos = g.calc_move()
            g.confirm_move(new_pos)
            g.make_syringe()
        g.escape()
    g.end_game()


if __name__ == "__main__":
    main()
