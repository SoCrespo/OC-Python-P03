class Maze:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
        self.background = self._background()
        self.exit = self._exit()
        self.corridor = {i:j for i, j in self.background.items() if j == "_"}
    

    def _background(self):
        background = dict()
        with open(self.pattern_path, "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                for j, letter in enumerate(line.strip()):
                    background.update({(i,j): letter})
        return background
        
    def _exit(self): 
        elements = self.background.values()    
        if ":" not in elements:
            raise ValueError("Le labyrinthe n'a pas de sortie")
        if list(elements).count(":") > 1:
            raise ValueError("Le labyrinthe a plus d'une sortie")     
        coord = [i for i,j in self.background.items() if j == ":"][0] 
        if coord in [(0,0), (0,14), (14,0), (14,14)]: # replace 14 by n ?
            raise ValueError("Sortie située dans un angle")
        return coord

    
            
if __name__ == "__main__":
     pass 
 
maze = Maze("pattern.txt")
print(maze.exit)

    