class Board():
    def __init__(self):
        n = 3
        self.board = [[[" " for k in range(n)]
                       for j in range(n)] for i in range(n)]

    def displayBoard(self):
        board = ""
        for i in range(3):
            board += "    --- --- ---\n"
            for j in range(3):
                board += (3-j)*" "
                board += "/"
                for k in range(3):
                    board += str(self.board[i][j][k])
                    board += " / "
                board += "\n"
                board += (3-j)*" "
                board += "--- --- ---\n"
            board += "\n"
        print(board)

    def checkEndGame(self, player):
        return None

    def placeMove(self, player, position):
        self.board[position[0]][position[1]//3][position[1] % 3] = player
        if (player != human):
            print("Computer placed moved at", position[0], position[1])


def getInputUser():
    layer = int(input("State the layer(0, 1, 2) you want to place your move: "))
    index = int(input("State the position(0-9) you want to place your move: "))
    return [layer, index]


def getInputAI(b, player):
    return [1, 1]


if __name__ == "__main__":
    b = Board()
    human = "X"
    b.displayBoard()
    player = "X"
    while True:
        move = getInputUser() if (player == human) else getInputAI(b, player)
        b.placeMove(player, move)
        b.displayBoard()
        endGame = b.checkEndGame(player)
        if (endGame != None):
            if (endGame):
                print(player, "won the game!")
            else:
                print("Tie")
            break
        player = "X" if (player == "O") else "O"
