from Board import Board

class GameTreeNode:
    MAX_DEPTH = 3  # Static constant

    def __init__(self, game_board, player):
        """Initialize a game tree node with a game state."""
        self.children = []  # List of child nodes
        self.game_board = game_board  # Stores the current game state
        self.minimax_value = 0  # Stores minimax evaluation
        self.depth = 0  # Stores the depth of the node in the tree
        self.player = player

    @staticmethod
    def isTerminal(board):
        return board.check_win() != 0
    
    @staticmethod
    def other_player(player):
        return 1 if player == 2 else 2

    def minimax (self, depth, isMaximizing):

        if depth == self.MAX_DEPTH or self.game_board.check_win() != 0:
            print(f"its the end... eval: {self.game_board.evaluate()}\n")
            return self.game_board.evaluate()

        if isMaximizing:  # Maximizing player (AI)
            print(f"max @ depth {depth}\n")
            bestScore = float('-inf')
        #     for each possible move in state:
        #         newState = applyMove(state, move)  // Generate new game state
        #         score = Minimax(newState, depth + 1, False)  // Recursive call for minimizing player
        #         bestScore = max(bestScore, score)  // Choose the highest score
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:
                        child_board = self.game_board.clone()
                        child_board.place_piece(i, j, self.player)
                        child_node = GameTreeNode(child_board, self.player)
                        child_node.game_board.print_board()
                        child_node.game_board.evaluate()
                        # score = child_node.minimax(depth + 1, False)
                        # bestScore = max(bestScore, score)

            print(f"max returning {bestScore}\n")
            return bestScore

        else:  # Minimizing player (Opponent)
            print(f"min @ depth {depth}\n")
            bestScore = float('inf')
        #     for each possible move in state:
        #         newState = applyMove(state, move)  // Generate new game state
        #         score = Minimax(newState, depth + 1, True)  // Recursive call for maximizing player
        #         bestScore = min(bestScore, score)  // Choose the lowest score
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:
                        child_board = self.game_board.clone()
                        child_board.place_piece(i, j, self.other_player(self.player))
                        child_node = GameTreeNode(child_board, self.player)
                        child_node.game_board.print_board()
                        child_node.game_board.evaluate()
                        # score = child_node.minimax(depth + 1, True)
                        # bestScore = min(bestScore, score)

            print(f"min returning {bestScore}\n")
            return bestScore
