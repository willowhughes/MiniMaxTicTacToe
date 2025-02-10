import copy

class Board:
    """This class deals with game board objects and related functionality"""
    X = 'X'
    O = 'O'
    SIZE = 3
    EMPTY = ' '
    
    def __init__(self):
        """Initializes a new board"""
        self.game_board = [[self.EMPTY, self.EMPTY, self.EMPTY],
                           [self.EMPTY, self.EMPTY, self.EMPTY],
                           [self.EMPTY, self.EMPTY, self.EMPTY]]

    def place_piece(self, row, col, player):
        """Places a piece on the board
        
        Returns: True on success, False on collision
        """
        if self.game_board[row][col] != self.EMPTY:
            print("That space is already occupied, try again.")
            return False
        if player == 1:
            self.game_board[row][col] = self.X
        else:
            self.game_board[row][col] = self.O
        return True

    def check_win(self):
        """retuns: 0 if nobody has won yet, 1 if player 1 (X) has won, 2 if player 2 (O) has won, 3 for draw"""
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
            
    def evaluate(self, player):
        """A heuristic function for the minimax algorithm

        X_2 represents the # of rows, columns and diagonals with 2 Xs and no Os
        X_1 represents the # of rows, columns and diagonals with 1 X and no Os
        ...so on so forth
        """
        X_3, X_2, X_1, O_3, O_2, O_1 = 0, 0, 0, 0, 0, 0
        
        #check diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][i] == self.X:
                X_count += 1
            elif self.game_board[i][i] == self.O:
                O_count += 1
        #Determine X_3, X_2, X_1, O_3, O_2, O_1 based on counts
        if X_count == 3 and O_count == 0:
            X_3 += 1
        elif X_count == 2 and O_count == 0:
            X_2 += 1
        elif X_count == 1 and O_count == 0:
            X_1 += 1
        if O_count == 3 and X_count == 0:
            O_3 += 1
        elif O_count == 2 and X_count == 0:
            O_2 += 1
        elif O_count == 1 and X_count == 0:
            O_1 += 1

        #check anti-diag
        X_count, O_count = 0, 0
        for i in range(self.SIZE):
            if self.game_board[i][(self.SIZE-1)-i] == self.X:
                X_count += 1
            elif self.game_board[i][(self.SIZE-1)-i] == self.O:
                O_count += 1
        if X_count == 3 and O_count == 0:
            X_3 += 1
        elif X_count == 2 and O_count == 0:
            X_2 += 1
        elif X_count == 1 and O_count == 0:
            X_1 += 1
        if O_count == 3 and X_count == 0:
            O_3 += 1
        elif O_count == 2 and X_count == 0:
            O_2 += 1
        elif O_count == 1 and X_count == 0:
            O_1 += 1

        #check rows
        for row in range(self.SIZE):
            X_count, O_count = 0, 0
            for col in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            if X_count == 3 and O_count == 0:
                X_3 += 1
            elif X_count == 2 and O_count == 0:
                X_2 += 1
            elif X_count == 1 and O_count == 0:
                X_1 += 1
            if O_count == 3 and X_count == 0:
                O_3 += 1
            elif O_count == 2 and X_count == 0:
                O_2 += 1
            elif O_count == 1 and X_count == 0:
                O_1 += 1
        
        #check columns
        for col in range(self.SIZE):
            X_count, O_count = 0, 0
            for row in range(self.SIZE):
                if self.game_board[row][col] == self.X:
                    X_count += 1
                elif self.game_board[row][col] == self.O:
                    O_count += 1
            if X_count == 3 and O_count == 0:
                X_3 += 1
            elif X_count == 2 and O_count == 0:
                X_2 += 1
            elif X_count == 1 and O_count == 0:
                X_1 += 1
            if O_count == 3 and X_count == 0:
                O_3 += 1
            elif O_count == 2 and X_count == 0:
                O_2 += 1
            elif O_count == 1 and X_count == 0:
                O_1 += 1

        if player == 1: # Heuristic function for player 1
            eval = 10*X_3 + 3*X_2 + X_1 - (10*O_3 + 3*O_2 + O_1)
        else:   # Heuristic function for player 2
            eval = 10*O_3 + 3*O_2 + O_1 - (10*X_3 + 3*X_2 + X_1)
        return eval

    def print_board(self):
        """Prints the game board to the console."""
        print("\n")
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                print(f" {self.game_board[i][j]}", end='')
                if j < self.SIZE-1:
                    print(" |", end='')
            if i < self.SIZE-1:
                print("\n---+---+---")
        print("\n")

    def clone(self):
        """Returns a copy of the passed in Board object."""
        boardCopy = copy.deepcopy(self)
        return boardCopy
