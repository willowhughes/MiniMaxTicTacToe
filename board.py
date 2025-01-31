class Board:
    X = 'X'
    O = 'O'
    SIZE = 3
    EMPTY = ' '
    gameBoard = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]

    
    def placePiece(self, row, col, player):
        if self.gameBoard[row][col] != self.EMPTY:
            print("That space is already occupied, try again.")
            return False
        if player == 1:
            self.gameBoard[row][col] = self.X
        else:
            self.gameBoard[row][col] = self.O
        return True

    def checkWin(self, player, row, col):
        tile = self.O
        if player == 1:
            tile = self.X
        #check col
        for i in range(self.SIZE):
            if self.gameBoard[i][col] != tile:
                break
            if i == self.SIZE - 1:
                return True
        #check row
        for i in range(self.SIZE):
            if self.gameBoard[row][i] != tile:
                break
            if i == self.SIZE-1:
                return True
        
        #check diag
        if row == col:
            #we're on a diagonal
            for i in range(self.SIZE):
                if self.gameBoard[i][i] != tile:
                    break
                if i == self.SIZE-1:
                    return True
            
        #check anti diag
        if row + col == self.SIZE - 1:
            for i in range(self.SIZE):
                if self.gameBoard[i][(self.SIZE-1)-i] != tile:
                    break
                if i == self.SIZE-1:
                    return True
        return False
            

    def evaluate():
        return 0

    def printBoard(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                print(f" {self.gameBoard[i][j]}", end='')
                if j < self.SIZE-1:
                    print(" |", end='')
            if i < self.SIZE-1:
                print("\n---+---+---")
        print("")

