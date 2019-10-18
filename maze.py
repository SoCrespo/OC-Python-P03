maze_background = dict()
with open("pattern.txt", "r", encoding = "utf8") as p:
    for i, line in enumerate(p):
        for j, letter in enumerate(line):
            maze_background.update({(i,j): letter})

for i in range(15):
    for j in range(15):
        print(maze_background.get((i,j)), end=" ")
    print("\n")
