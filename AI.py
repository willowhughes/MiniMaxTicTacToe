from Board import Board

class AI:
    MAX_DEPTH = 3  # Static constant

    def __init__(self, player):
        """Initialize a game tree node with a game state."""
        self.minimax_value = 0  # Stores minimax evaluation
        self.depth = 0  # Stores the depth of the node in the tree
        self.player = player

    @staticmethod
    def isTerminal(board):
        return board.check_win() != 0
    
    @staticmethod
    def other_player(player):
        return 1 if player == 2 else 2

    def minimax (self, board, depth, isMaximizing):

        if depth == self.MAX_DEPTH or board.check_win() != 0:
            print("its the end\n" + board.evaluate() + "\n")
            return board.evaluate()

        if isMaximizing:  # Maximizing player (AI)
            print(f"max @ depth {depth}\n")
            bestScore = float('-inf')
        #     for each possible move in state:
        #         newState = applyMove(state, move)  // Generate new game state
        #         score = Minimax(newState, depth + 1, False)  // Recursive call for minimizing player
        #         bestScore = max(bestScore, score)  // Choose the highest score
            for i in range(board.SIZE):
                for j in range(board.SIZE):
                    if board.game_board[i][j] == board.EMPTY:
                        child_board = board.clone()
                        child_board.place_piece(i, j, self.player)
                        child_board.print_board()

            print(f"max returning {bestScore}\n")
            return bestScore

        else:  # Minimizing player (Opponent)
            print(f"min @ depth {depth}\n")
            bestScore = float('inf')
        #     for each possible move in state:
        #         newState = applyMove(state, move)  // Generate new game state
        #         score = Minimax(newState, depth + 1, True)  // Recursive call for maximizing player
        #         bestScore = min(bestScore, score)  // Choose the lowest score
            for i in range(board.SIZE):
                for j in range(board.SIZE):
                    if board.game_board[i][j] == board.EMPTY:
                        #print(f"(min) potential move at: {i}, {j}\n")
                        child_board = board.clone()
                        child_board.place_piece(i, j, self.other_player(self.player))
                        child_board.print_board()

            print(f"min returning {bestScore}\n")
            return bestScore