import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    

print("")

playerchoice = input("Enter...\n1 for Rock,\n2 for paper,or \n3 for scissors:\n\n")


player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1, 2, or 3.") 
    

computer_choice = random.choice("123")
computer = int(computer_choice)


print("")

print("You choose "+ str(RPS(player)).replace('RPS', '') + ".")
print("Python choose "+ str(RPS(computer)).replace("RPS", ''), ".")
print("")


if player == 1 or computer == 3:
    print("😍 You win!")
elif player == 2 and computer == 1:
    print("😍 You win!")
elif player == 3 and computer == 2:
    print("😍 You win!")
elif player == computer:
    print("😍 Tie game!")
else:
    print("🐍 Python wins!")

   
