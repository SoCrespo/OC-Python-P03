class Maze:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
        self.background = self.set_background()
        self.exit = self.get_exit()

    def set_background(self):
        background = dict()
        with open(self.pattern_path, "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                for j, letter in enumerate(line.strip()):
                    background.update({(i,j): letter})
        return background
        
    def get_exit(self): 

        def exactly_one_exit(self):
            elements = self.background.values()    
            if ":" not in elements:
                raise ValueError("Le labyrinthe n'a pas de sortie")
                return False
            if list(elements).count(":") > 1:
                raise ValueError("Le labyrinthe a plus d'une sortie")
                return False
            else:
                return True

        if exactly_one_exit(self):               
            return [i for i,j in self.background.items() if j == ":"][0]

    if __name__ == "__main__":
        pass
