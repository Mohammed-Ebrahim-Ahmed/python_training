import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    def play_rps():

        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter...\n1 for Rock,\n2 for paper,or \n3 for scissors:\n\n"
        )
        if int(playerchoice) not in [1, 2, 3]:
            print("You must enter 1, 2 or 3.")
            return play_rps()

        player = int(playerchoice)
        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print("You choose " + str(RPS(player)).replace("RPS.", "").title() + ".")
        print("Python choose " + str(RPS(computer)).replace("RPS.", "").title() + ".\n")
        def decide_winner(player, computer):
            
            nonlocal player_wins
            nonlocal python_wins
            
            if player == RPS.ROCK and computer == RPS.SCISSORS:
                player_wins += 1
                return "😍 You win!"
                
            elif player == RPS.PAPER and computer == RPS.ROCK:
                player_wins += 1
                return "😍 You win!"
                
            elif player == RPS.SCISSORS and computer == RPS.PAPER:
                player_wins += 1
                return "😍 You win!"
                
            elif player == computer:
                return "🤫 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
        nonlocal game_count
        game_count += 1
        
        print("\nGame Count: " + str(game_count))
        print("\nPlayer Count: " + str(player_wins))
        print("\nPython Count: " + str(python_wins))
        print("\nPlay again?")

        while True:
            # Ask the user if they want to play again
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        elif playagain.lower() == "q":
            print("\n Thank you")
            # Exit the game
            sys.exit("\nBye! 😪")
            
    return play_rps

play = rps()
play()