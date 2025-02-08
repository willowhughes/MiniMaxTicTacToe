import copy

class Board:
    X = 'X'
    O = 'O'
    SIZE = 3
    EMPTY = ' '
    game_board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]

    
    def place_piece(self, row, col, player):
        if self.game_board[row][col] != self.EMPTY:
            print("That space is already occupied, try again.")
            return False
        if player == 1:
            self.game_board[row][col] = self.X
        else:
            self.game_board[row][col] = self.O
        return True

    # retuns: 0 if nobody has won yet, 1 if player 1 (X) has won, 2 if player 2 (O) has won, 3 for draw
    def check_win(self):
        
        #check diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][i] == self.X:
                X_count += 1
            elif self.game_board[i][i] == self.O:
                O_count += 1
        if X_count == 3:
            return 1
        elif O_count == 3:
            return 2

        #check anti-diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][(self.SIZE-1)-i] == self.X:
                X_count += 1
            elif self.game_board[i][(self.SIZE-1)-i] == self.O:
                O_count += 1
        if X_count == 3:
            return 1
        elif O_count == 3:
            return 2

        #check rows
        for row in range(self.SIZE):
            X_count, O_count = 0, 0
            for col in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            if X_count == 3:
                return 1
            elif O_count == 3:
                return 2
        
        #check columns
        for col in range(self.SIZE):
            X_count, O_count = 0, 0
            for row in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            if X_count == 3:
                return 1
            elif O_count == 3:
                return 2
            
        # check draw
        empty_spaces = 9
        for col in range(self.SIZE):
            for row in range(self.SIZE):
                if self.game_board[row][col] != self.EMPTY:
                    empty_spaces -= 1
        if empty_spaces == 0:
            return 3     
            
        return 0
            
    def evaluate(self):
        #X_2 represents the # of rows, columns and diagonals with 2 Xs and no Os
        #X_1 represents the # of rows, columns and diagonals with 1 X and no Os
        #same for O_2 and O_1
        X_2, X_1, O_2, O_1 = 0, 0, 0, 0
        
        #check diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][i] == self.X:
                X_count += 1
            elif self.game_board[i][i] == self.O:
                O_count += 1
        #Determine X_2, X_1, O_2, O_1 based on counts
        if X_count == 2 and O_count == 0:
            X_2 += 1  # Diag has 2 Xs and no Os
        elif X_count == 1 and O_count == 0:
            X_1 += 1  # Diag has 1 X and no Os
        if O_count == 2 and X_count == 0:
            O_2 += 1  # Diag has 2 Os and no Xs
        elif O_count == 1 and X_count == 0:
            O_1 += 1  # Diag has 1 O and no Xs

        #check anti-diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][(self.SIZE-1)-i] == self.X:
                X_count += 1
            elif self.game_board[i][(self.SIZE-1)-i] == self.O:
                O_count += 1
        #Determine X_2, X_1, O_2, O_1 based on counts
        if X_count == 2 and O_count == 0:
            X_2 += 1  # Diag has 2 Xs and no Os
        elif X_count == 1 and O_count == 0:
            X_1 += 1  # Diag has 1 X and no Os
        if O_count == 2 and X_count == 0:
            O_2 += 1  # Diag has 2 Os and no Xs
        elif O_count == 1 and X_count == 0:
            O_1 += 1  # Diag has 1 O and no Xs

        #check rows
        for row in range(self.SIZE):
            X_count, O_count = 0, 0
            for col in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            # Determine X_2, X_1, O_2, O_1 based on counts
            if X_count == 2 and O_count == 0:
                X_2 += 1  # row has 2 Xs and no Os
            elif X_count == 1 and O_count == 0:
                X_1 += 1  # row has 1 X and no Os
            if O_count == 2 and X_count == 0:
                O_2 += 1  # row has 2 Os and no Xs
            elif O_count == 1 and X_count == 0:
                O_1 += 1  # row has 1 O and no Xs
        
        #check columns
        for col in range(self.SIZE):
            X_count, O_count = 0, 0
            for row in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            # Determine X_2, X_1, O_2, O_1 based on counts
            if X_count == 2 and O_count == 0:
                X_2 += 1  # Column has 2 Xs and no Os
            elif X_count == 1 and O_count == 0:
                X_1 += 1  # Column has 1 X and no Os
            if O_count == 2 and X_count == 0:
                O_2 += 1  # Column has 2 Os and no Xs
            elif O_count == 1 and X_count == 0:
                O_1 += 1  # Column has 1 O and no Xs

        #print(f"x2={X_2} x1={X_1} o2={O_2} o1={O_1}")
        eval = 3*O_2+O_1-(3*X_2+X_1)
        print(f"evaluation = {eval}")
        return eval

    def print_board(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                print(f" {self.game_board[i][j]}", end='')
                if j < self.SIZE-1:
                    print(" |", end='')
            if i < self.SIZE-1:
                print("\n---+---+---")
        print("")

    def clone(self):
        boardCopy = copy.deepcopy(self)
        return boardCopy

