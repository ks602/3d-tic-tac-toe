class Board():
    def __init__(self):
        self.n = 3
        self.board = [[[" " for k in range(self.n)]
                       for j in range(self.n)] for i in range(self.n)]
        # self.board = [
        #     [[" ", " ", " "],
        #      [" ", " ", " "],
        #      ["X", " ", " "]],

        #     [[" ", " ", " "],
        #      ["X", " ", " "],
        #      [" ", " ", " "]],

        #     [["X", " ", " "],
        #      [" ", " ", " "],
        #      [" ", " ", " "]]]

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

    def checkWinGame(self, player, move):
        layer = move[0]
        x = move[1]//3
        y = move[1] % 3

        # check same layer
        # check row
        for i in range(self.n):
            if (self.board[layer][x][i] != player):
                break
            if (i == self.n-1):
                return True

        # check column
        for i in range(self.n):
            if (self.board[layer][i][y] != player):
                break
            if (i == self.n-1):
                return True

        # check diagonal
        if (x == y):
            for i in range(self.n):
                if (self.board[layer][i][i] != player):
                    break
                if (i == self.n-1):
                    return True

        # check anti-diagonal:
        if (x+y == self.n-1):
            for i in range(self.n):
                if (self.board[layer][i][self.n-1-i] != player):
                    break
                if (i == self.n-1):
                    return True

        # check across layer
        # check vertical
        for i in range(self.n):
            if (self.board[i][x][y] != player):
                break
            if (i == self.n-1):
                return True

        # check diagonal in y-axis
        if (layer == x):
            for i in range(self.n):
                if (self.board[i][i][y] != player):
                    break
                if (i == self.n-1):
                    return True

        # check anti-diagonal in y-axis
        if (layer+x == self.n-1):
            for i in range(self.n):
                if (self.board[i][self.n-1-i][y] != player):
                    break
                if (i == self.n-1):
                    return True

        # check diagonal in x-axis
        if (layer == y):
            for i in range(self.n):
                if (self.board[i][x][i] != player):
                    break
                if (i == self.n-1):
                    return True

        # check anti-diagonal in x-axis
        if (layer+y == self.n-1):
            for i in range(self.n):
                if (self.board[i][x][self.n-1-i] != player):
                    break
                if (i == self.n-1):
                    return True

        # check diagonal from (0,0,0) to (2,2,2)
        if (layer == x == y):
            for i in range(self.n):
                if (self.board[i][i][i] != player):
                    break
                if (i == self.n-1):
                    return True

        # check diagonal from (0,0,2) to (2,2,0)
        for i in range(self.n):
            if (self.board[i][i][self.n-1-i] != player):
                break
            if (i == self.n-1):
                return True

        # check diagonal from (0,2,0) to (2,0,2)
        for i in range(self.n):
            if (self.board[i][self.n-1-i][i] != player):
                break
            if (i == self.n-1):
                return True

        # check diagonal from (0,2,2) to (2,0,0)
        if (x == y):
            for i in range(self.n):
                if (self.board[i][self.n-1-i][self.n-1-i] != player):
                    break
                if (i == self.n-1):
                    return True
        return False

    def checkEndGame(self):
        for layer in self.board:
            for row in layer:
                for cell in row:
                    if (cell == " "):
                        return False
        return True

    def placeMove(self, player, move):
        if (move[0] > 2 or move[0] < 0):
            return False
        if (move[1] > 8 or move[0] < 0):
            return False
        if (self.board[move[0]][move[1]//3][move[1] % 3] != " "):
            return False
        self.board[move[0]][move[1]//3][move[1] % 3] = player
        if (player != human):
            print("Computer placed moved at", move[0], move[1])
        return True


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
        while True:
            move = getInputUser() if (player == human) else getInputUser()
            if (b.placeMove(player, move)):
                break
        b.displayBoard()
        won = b.checkWinGame(player, move)
        if (won):
            print(player, "won the game!")
            break

        endGame = b.checkEndGame()
        if (endGame):
            print("Tie!")
            break
        player = "X" if (player == "O") else "O"
