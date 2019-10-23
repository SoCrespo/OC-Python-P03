class Hero():
    def __init__(self, name, coord):
        self.name = name
        self.bag = []
        self.coord = coord
        #self.image = image
        
if __name__ == "__main__":
    player = Hero("MacGyver")
    print(player.name)
