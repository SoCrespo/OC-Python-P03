import random

import maze
import item
import hero

class Game:
    
    def __init__(self):
        pass
    
    the_maze = maze.Maze("pattern.txt")

    mac_gyver = hero.Hero("MacGyver")
    guard = item.Item("Guard")
    needle = item.Item("Needle")
    tube = item.Item("Tube")
    ether = item.Item("Ether")

    tools_positions = random.choices(list(the_maze.corridor.keys()), k=3)

    items_positions = {
        mac_gyver : the_maze.mac_pos, 
        guard : the_maze.exit_pos, 
        needle : tools_positions[0],
        tube : tools_positions[1],
        ether : tools_positions[2], 
        }

    # def update_item_pos(background, items_positions):      
    #     for item, pos in items_positions.items():
    #         background[.update(i)]


