import random

import maze
import item
import tool


the_maze = maze.Maze("pattern.txt")

mac_gyver = item.Hero()
guard = item.Item()
needle = item.Item()
tube = item.Item()
ether = item.Item()

tools_positions = random.choices(list(the_maze.corridor.keys()), k=3)

items_positions = {
    mac_gyver : (1,1), 
    guard : the_maze.exit, 
    needle : tools_positions[0],
    tube : tools_positions[1],
    ether : tools_positions[2], 
    }

      
  


