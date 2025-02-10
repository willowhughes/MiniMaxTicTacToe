from Board import Board

class GameTreeNode:
    """This class handling the MINIMAX AI algorithm for tictactoe"""
    MAX_DEPTH = 3

    def __init__(self, game_board, player):
        """Initializes a new GameTreeNode object with the given game board and player."""
        self.game_board = game_board
        self.minimax_value = 0
        self.player = player
        self.nodes_expanded = 0

    @staticmethod
    def isTerminal(board):
        """Returns True if the game is over, False otherwise."""
        return board.check_win() != 0
    
    @staticmethod
    def other_player(player):
        """Returns 1 if 2 is passed in or returns 2 if 1 is passed in"""
        return 1 if player == 2 else 2

    def minimax (self, depth, is_maximizing):
        """An implementation of the minimax algorithm with depth-limited search
        
        returns: the best score, the row of the best move, and the column of the best move
        """
        # Base case: if the game is over or the maximum depth is reached
        if depth == self.MAX_DEPTH or self.game_board.check_win() != 0:
            self.nodes_expanded += 1
            return self.game_board.evaluate(self.player), None, None
        
        best_move = None

        if is_maximizing:  # Maximizing player (AI)
            best_score = float('-inf')
            # Loop through all possible moves
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:   # If the space is empty
                        child_board = self.game_board.clone()   # Clone the board and Place the appropriate piece
                        child_board.place_piece(i, j, self.player)
                        child_node = GameTreeNode(child_board, self.player) # Create a new node with the new board
                        score, _, _ = child_node.minimax(depth + 1, False)  # Recursively call minimax
                        self.nodes_expanded += child_node.nodes_expanded    # Accumulate expanded nodes
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move[0], best_move[1]

        else:   # Minimizing player (Opponent)
            best_score = float('inf')
            # Loop through all possible moves
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:
                        child_board = self.game_board.clone()
                        child_board.place_piece(i, j, self.other_player(self.player))
                        child_node = GameTreeNode(child_board, self.player)
                        score, _, _ = child_node.minimax(depth + 1, True)
                        self.nodes_expanded += child_node.nodes_expanded
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move[0], best_move[1]
