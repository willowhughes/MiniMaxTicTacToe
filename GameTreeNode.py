from Board import Board

class GameTreeNode:
    MAX_DEPTH = 3

    def __init__(self, game_board, player): # Initialize a game tree node with a game state
        self.game_board = game_board  # Stores the current game state
        self.minimax_value = 0  # Stores minimax evaluation
        self.player = player

    @staticmethod
    def isTerminal(board):
        return board.check_win() != 0
    
    @staticmethod
    def other_player(player):
        return 1 if player == 2 else 2

    def minimax (self, depth, is_maximizing):

        if depth == self.MAX_DEPTH or self.game_board.check_win() != 0:
            self.game_board.print_board()
            print(f"its the end... eval: {self.game_board.evaluate()}\n")
            return self.game_board.evaluate(), None, None
        
        best_move = None

        if is_maximizing:  # Maximizing player (AI)
            best_score = float('-inf')
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:
                        child_board = self.game_board.clone()
                        child_board.place_piece(i, j, self.player)
                        child_node = GameTreeNode(child_board, self.player)
                        score, _, _ = child_node.minimax(depth + 1, False)
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            # print(f"max returning {best_score}, {best_move}\n")
            return best_score, best_move[0], best_move[1]

        else:  # Minimizing player (Opponent)
            best_score = float('inf')
            for i in range(self.game_board.SIZE):
                for j in range(self.game_board.SIZE):
                    if self.game_board.game_board[i][j] == self.game_board.EMPTY:
                        child_board = self.game_board.clone()
                        child_board.place_piece(i, j, self.other_player(self.player))
                        child_node = GameTreeNode(child_board, self.player)
                        score, _, _ = child_node.minimax(depth + 1, True)
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
            # print(f"min returning {best_score}, {best_move}\n")
            return best_score, best_move[0], best_move[1]
