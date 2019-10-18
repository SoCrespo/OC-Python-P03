class Maze:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
    
        background = dict()
        with open(self.pattern_path, "r", encoding = "utf8") as p:
            for i, line in enumerate(p):
                for j, letter in enumerate(line):
                    background.update({(i,j): letter})
        self.background = background
