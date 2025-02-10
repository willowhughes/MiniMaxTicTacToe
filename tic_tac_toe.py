import Game

"""
tic_tac_toe.py

This module implements a Tic-Tac-Toe game with both Human vs. AI and AI vs. AI modes. 
The AI uses the Minimax algorithm with a depth-limited search to determine the best move.

Classes:
    GameTreeNode: Implements the Minimax algorithm for the AI.
    Board: Manages the game board and related functionality.
    Game: Handles running the game, including user input and game flow.

Usage:
    Run this script to start the game. You can choose to play against the AI or watch two AIs play against each other.

Example:
    $ python tic_tac_toe.py

Author:
    Willow Hughes
"""

Game.start_game()
