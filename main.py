import Game

choice = input("=====================================\n\nSelect the AIs opponent:\n[1] Human\n[2] AI\n==>: ")
if choice == "1":
    Game.play_game()
elif choice == "2":
    Game.play_game_ai()