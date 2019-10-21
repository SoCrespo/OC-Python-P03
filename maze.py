class Maze:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
        self.background = self._background()
        self.corridor = {i:j for i, j in self.background.items() if j == "_"}
        self.mac_pos, self.exit_pos = self._get_pos()

    def _background(self):
        background = dict()
        with open(self.pattern_path, "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                for j, letter in enumerate(line.strip()):
                    background.update({(i,j): letter})
        return background
        
    def _get_pos(self): 
        elements = self.background.items()
        mac_pos = []
        exit_pos = []
        for coord, item in elements:
            if item == "*":
                mac_pos.append(coord)
            elif item == ":":
                exit_pos.append(coord)    
        if len(mac_pos) == len(exit_pos) == 1 :
            return mac_pos[0], exit_pos[0]
        raise ValueError("Erreur sur position de MacGyver ou de la sortie")
            
           
            
if __name__ == "__main__":
    maze = Maze("pattern.txt")
    print(maze.background)
    print(maze.mac_pos, maze.exit_pos)
    
    