from Board import Board
from GameTreeNode import GameTreeNode
from AI import AI

def play_game():
    board = Board()
    moveCount = 0
    player = 1

    while True:
        board.print_board()
        print(f"Evaluation = {board.evaluate()}")
        player = moveCount % 2 + 1
        print(f"Player {player}'s turn...")

        if player == 1:
            successful_move = False
            while successful_move == False:
                row = get_input_coordinate("row")
                col = get_input_coordinate("column")
                successful_move = board.place_piece(row, col, player)
        else:
            print(f"\nDebugging AI (player {player})...\n-------------------------------------\n")

            node = GameTreeNode(board, player)
            _, row, col = node.minimax(0, True)
            board.place_piece(row, col, player)

            print("\n-------------------------------------\n")

        
        print("=====================================")
        status = board.check_win()
        if status == 3:
            board.print_board()
            print(f"\nDraw! {player} wins!\n=====================================\n")
            break
        if status == 1 or status == 2:
            board.print_board()
            print(f"\nPlayer {player} wins!\n=====================================\n")
            break
        moveCount += 1
            
@staticmethod
def get_input_coordinate(axis):
    while True:
        userInput = input(f"Enter {axis} (0 to 2): ")
        try:
            number = int(userInput)
            if number < 0 or number > 2:
                print("That's not in bounds (0 to 2)")
                continue
            return number
        except ValueError:
            print("That's not a number!")