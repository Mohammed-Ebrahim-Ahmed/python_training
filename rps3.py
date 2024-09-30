import sys
import random
from enum import Enum


def play_rps():

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


play_rps()
