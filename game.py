from Board import Board
from GameTreeNode import GameTreeNode
import time
import sys

THINKING_TIME_MULTIPLIER = 1

def play_game():
    board = Board()
    moveCount = 0
    player = 1

    while True:
        print("\n=====================================")
        board.print_board()
        status = board.check_win()
        if status == 3:
            print(f"\nDraw!\n=====================================\n")
            break
        if status == 1 or status == 2:
            print(f"\nPlayer {player} wins!\n=====================================\n")
            break

        player = moveCount % 2 + 1
        print(f"Player {player}'s turn...")

        if player == 1:
            successful_move = False
            while successful_move == False:
                row = get_input_coordinate("row")
                col = get_input_coordinate("column")
                successful_move = board.place_piece(row, col, player)
        else:
            # print(f"\nDebugging AI (player {player})...\n-------------------------------------\n")

            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            board.place_piece(row, col, player)

            # print("\n-------------------------------------\n")

        moveCount += 1

def play_game_ai():
    board = Board()
    moveCount = 0
    player = 1

    while True:
        print("\n=====================================")
        board.print_board()
        status = board.check_win()
        if status == 3:
            print(f"\nDraw!\n=====================================\n")
            break
        if status == 1 or status == 2:
            print(f"\nPlayer {player} wins!\n=====================================\n")
            break

        player = moveCount % 2 + 1
        print(f"Player {player}'s turn...")

        if player == 1:
            # print(f"\nDebugging AI (player {player})...\n-------------------------------------\n")

            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            board.place_piece(row, col, player)

            # print("\n-------------------------------------\n")
        else:
            # print(f"\nDebugging AI (player {player})...\n-------------------------------------\n")

            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            board.place_piece(row, col, player)

            # print("\n-------------------------------------\n")

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

@staticmethod
def simulate_thinking():
    for i in range(4):  # Loop through thinking stages
        sys.stdout.write("\rThinking" + "." * i + "   ")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(THINKING_TIME_MULTIPLIER*0.5)
    print("\n")