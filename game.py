from board import Board

def playGame():
    board = Board()
    moveCount = 0
    player = 1

    while True:
        board.printBoard()
        board.evaluate()
        player = moveCount % 2 + 1
        print(f"Player {player}'s turn...")

        success = False
        while success == False:
            row = getInputCoordinate("row")
            col = getInputCoordinate("column")
            success = board.placePiece(row, col, player)
        
        print("\n=====================================\n")
        moveCount += 1
        if board.checkWin(player, row, col):
            board.printBoard()
            print(f"\nPlayer {player} wins!\n=====================================\n")
            break
        if moveCount == (board.SIZE ** 2):
            board.printBoard()
            print(f"\nDRAW\n=====================================\n")
            break
            

def getInputCoordinate(axis):
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