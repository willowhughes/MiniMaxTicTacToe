import copy

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
            
    def evaluate(self):
        X_2, X_1, O_2, O_1 = 0, 0, 0, 0
        
        #check diag
        XCount, OCount = 0, 0
        for i in range(self.SIZE):
            if self.gameBoard[i][i] == self.X:
                XCount += 1
            elif self.gameBoard[i][i] == self.O:
                OCount += 1
        #Determine X_2, X_1, O_2, O_1 based on counts
        if XCount == 2 and OCount == 0:
            X_2 += 1  # Diag has 2 Xs and no Os
        elif XCount == 1 and OCount == 0:
            X_1 += 1  # Diag has 1 X and no Os
        if OCount == 2 and XCount == 0:
            O_2 += 1  # Diag has 2 Os and no Xs
        elif OCount == 1 and XCount == 0:
            O_1 += 1  # Diag has 1 O and no Xs
        #print(f"X={XCount} O={OCount}")

        #check anti-diag
        XCount, OCount = 0, 0
        for i in range(self.SIZE):
            if self.gameBoard[i][(self.SIZE-1)-i] == self.X:
                XCount += 1
            elif self.gameBoard[i][(self.SIZE-1)-i] == self.O:
                OCount += 1
        #Determine X_2, X_1, O_2, O_1 based on counts
        if XCount == 2 and OCount == 0:
            X_2 += 1  # Diag has 2 Xs and no Os
        elif XCount == 1 and OCount == 0:
            X_1 += 1  # Diag has 1 X and no Os
        if OCount == 2 and XCount == 0:
            O_2 += 1  # Diag has 2 Os and no Xs
        elif OCount == 1 and XCount == 0:
            O_1 += 1  # Diag has 1 O and no Xs
        #print(f"X={XCount} O={OCount}")

        #check rows
        for row in range(self.SIZE):
            XCount, OCount = 0, 0
            for col in range(self.SIZE):
                #print(f"row={row} col={col} tile={self.gameBoard[row][col]}")
                if self.gameBoard[row][col] == self.X:
                    XCount += 1
                elif self.gameBoard[row][col] == self.O:
                    OCount += 1
            # Determine X_2, X_1, O_2, O_1 based on counts
            if XCount == 2 and OCount == 0:
                X_2 += 1  # row has 2 Xs and no Os
            elif XCount == 1 and OCount == 0:
                X_1 += 1  # row has 1 X and no Os
            if OCount == 2 and XCount == 0:
                O_2 += 1  # row has 2 Os and no Xs
            elif OCount == 1 and XCount == 0:
                O_1 += 1  # row has 1 O and no Xs
            #print(f"X={XCount} O={OCount}")
        
        #check columns
        for col in range(self.SIZE):
            XCount, OCount = 0, 0
            for row in range(self.SIZE):
                #print(f"row={row} col={col} tile={self.gameBoard[row][col]}")
                if self.gameBoard[row][col] == self.X:
                    XCount += 1
                elif self.gameBoard[row][col] == self.O:
                    OCount += 1
            # Determine X_2, X_1, O_2, O_1 based on counts
            if XCount == 2 and OCount == 0:
                X_2 += 1  # Column has 2 Xs and no Os
            elif XCount == 1 and OCount == 0:
                X_1 += 1  # Column has 1 X and no Os
            if OCount == 2 and XCount == 0:
                O_2 += 1  # Column has 2 Os and no Xs
            elif OCount == 1 and XCount == 0:
                O_1 += 1  # Column has 1 O and no Xs
            #print(f"X={XCount} O={OCount}")

        print(f"x2={X_2} x1={X_1} o2={O_2} o1={O_1}")
        eval = 3*X_2+X_1-(3*O_2+O_1)
        print(f"evaluation = {eval}")
        return eval

    def printBoard(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                print(f" {self.gameBoard[i][j]}", end='')
                if j < self.SIZE-1:
                    print(" |", end='')
            if i < self.SIZE-1:
                print("\n---+---+---")
        print("")

    def clone(self):
        boardCopy = copy.deepcopy(self)
        return boardCopy

