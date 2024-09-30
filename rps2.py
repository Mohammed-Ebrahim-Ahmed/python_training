import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for paper,or \n3 for scissors:\n\n"
    )
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1, 2, or 3.")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("You choose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python choose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == RPS.ROCK and computer == RPS.SCISSORS:
        print("😍 You win!")
    elif player == RPS.PAPER and computer == RPS.ROCK:
        print("😍 You win!")
    elif player == RPS.SCISSORS and computer == RPS.PAPER:
        print("😍 You win!")
    elif player == computer:
        print("🤫 Tie game!")
    else:
        print("🐍 Python wins!")

    # Ask the user if they want to play again
    playagain = input("\nPlay again? \nY for Yes or \nQ to quit: ")
    if playagain.lower() == "y":
        continue
    else:
        print("\n🔥🔥🔥🔥🔥🔥🔥")
        print("Thank you for playing!\n")
        playagain = False  # Proper indentation here

# Exit the game
sys.exit("Bye! 😪")
