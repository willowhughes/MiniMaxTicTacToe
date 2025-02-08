from Board import Board

class GameTreeNode:
    MAX_DEPTH = 3  # Static constant

    def __init__(self, game_board, player):
        """Initialize a game tree node with a game state."""
        self.children = []  # List of child nodes
        self.game_board = game_board  # Stores the current game state
        self.minimax_value = 0  # Stores minimax evaluation
        self.player = player

    def expand_children(self, depth_limit):
        """Expands game tree to the given depth limit."""
        # Implementation here
        pass

    def minimax(self, max):
        winner = self.game_board.check_win(self.game_board.board)

        if winner == 3: # Draw
            return 0
        elif winner == self.player: # AI wins
            return 1
        elif winner != self.player and winner != 0: # AI's opponent wins
            return -1
        
        if max:  # maximizing player
            best_score = float('-inf')
            for row in range(self.game_board.SIZE):
                for col in range(self.game_board.SIZE):
                    if self.game_board.board[row][col] == " ":
                        # Clone the board and make the move
                        new_board = clone_board(board)
                        new_board[row][col] = "X"
                        score = minimax(new_board, depth + 1, False)
                        best_score = max(best_score, score)
            return best_score
        
        else:  # minimizing player
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        # Clone the board and make the move
                        new_board = clone_board(board)
                        new_board[row][col] = "O"
                        score = minimax(new_board, depth + 1, True)
                        best_score = min(best_score, score)
            return best_score

