#! /usr/bin/env python3
# coding: utf-8

"""
Main function for Mac Gyver Game.
"""

import maze
import hero
import toolmanager
import pygameinterface
import params as pm


class Game:
    """Manages MacGyver Maze game"""

    def __init__(self):
        # Create Pygame interface
        self.pgi = pygameinterface.Pygameinterface()
        # Create player
        self.mac = hero.Hero()

    def initialize_game(self):
        '''
        Initialize tools positions, player's bag and syringe state
        to start new game.
        '''
        # Create laby from txt pattern
        self.laby = maze.Maze(pm.PATTERN)
        # Create object managing tools (random position, picking)
        self.tman = toolmanager.ToolManager(self.laby, self.mac)
        # Set player starting position from pattern
        self.mac.pos = self.laby.start_pos
        # Empty player's bag
        self.mac.bag = []
        # Player has no syringe at beginning
        self.syringe = False

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
        self.tman.add_tools_in_maze()

    def display_graphic_layer(self):
        '''
        Start pygame interface and display the game deck.
        '''
        self.pgi.open_game()
        self.pgi.display_layout(self.laby)

    def calc_move(self):
        ''' Calculates player new coordinates according to pressed key.'''
        action_switch = {
            "escape": self.pgi.quit_game,
            "up": self.mac.up,
            "down": self.mac.down,
            "left": self.mac.left,
            "right": self.mac.right,
        }
        while self.mac.pos != self.laby.exit:
            key = self.pgi.press_key()
            return action_switch.get(key)()

    def confirm_move(self, coord):
        '''Move player logically and graphically.'''
        if coord in self.laby.corridor:
            self.laby.move_player(self.mac, coord)
            self.mac.update_pos(coord)
            self.pgi.display_layout(self.laby)

    def pick_tool(self):
        '''If there's a tool, put it in player's bag and out of maze.'''
        self.tman.update_player_bag()

    def make_syringe(self):
        '''Make syringe when 3 tools are in player's bag.'''
        if not self.syringe:
            self.pgi.display_bag(self.mac.bag, self.laby)
            if len(self.mac.bag) == 3:
                self.pgi.wait(500)
                self.pgi.display_syringe(self.laby)
                self.syringe = True

    def exit_reached(self):
        '''Boolean : player is or not on the exit'''
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

    def main(self):
        '''Main loop of the game.'''
        while True:
            self.show_start_menu()
            if not self.want_to_play():
                break
            self.initialize_game()
            while not self.exit_reached():
                self.add_tools_in_maze()
                self.display_graphic_layer()
                new_pos = self.calc_move()
                self.confirm_move(new_pos)
                self.pick_tool()
                self.make_syringe()
            self.escape()
        self.end_game()


if __name__ == "__main__":
    g = Game()
    g.main()
