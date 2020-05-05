def displayBoard(grid):
    for layer in grid:
        for row in layer:
            for cell in row:
                print(cell, "/", end="")
            print()
            print("—— —— ——")
    print()


def initBoard():
    n = 3
    grid = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    return grid


if __name__ == "__main__":
    grid = initBoard()
    print(grid)
    displayBoard(grid)
