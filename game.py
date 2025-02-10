from Board import Board
from GameTreeNode import GameTreeNode
import time
import sys

"""This class handles running the game"""

THINKING_TIME_MULTIPLIER = 1

def start_game():
    """Runs a Human vs. AI game or AI vs. AI game"""
    while True:
        choice = input("=====================================\n\nSelect the AIs opponent:\n[1] Human\n[2] AI\n[3] Quit\n==>: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            play_game_ai()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.")

def play_game():
    """Runs the Human vs. AI tictactoe game"""
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
            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            print(f"nodes expanded: {node.nodes_expanded}")
            board.place_piece(row, col, player)

        moveCount += 1

def play_game_ai():
    """Runs the AI vs. AI tictactoe game"""
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
            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            print(f"nodes expanded: {node.nodes_expanded}")
            board.place_piece(row, col, player)
        else:
            node = GameTreeNode(board, player)
            score, row, col = node.minimax(0, True)
            simulate_thinking()
            print(f"AI Player {player} chose: {row}, {col}\n")
            print(f"nodes expanded: {node.nodes_expanded}")
            board.place_piece(row, col, player)

        moveCount += 1
            
@staticmethod
def get_input_coordinate(axis):
    """Takes in the Axis (row or col) as an arguement and gets coordinate input"""
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
    """A function for simulating time for the AI to think"""
    for i in range(4):  # Loop through thinking stages
        sys.stdout.write("\rThinking" + "." * i + "   ")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(THINKING_TIME_MULTIPLIER*0.5)
    print("\n")