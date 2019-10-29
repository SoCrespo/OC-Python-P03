class Hero:
    def __init__(self):
       self.pos = (1,1)
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