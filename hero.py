class Hero:
    def __init__(self):
        pass
    
    def up(self, coord):
        x, y = coord
        return (x - 1, y)

    def down(self, coord):
        x, y = coord
        return (x + 1, y)    

    def left(self, coord):
        x, y = coord
        return (x, y - 1)

    def right(self, coord):
        x, y = coord
        return (x, y + 1)