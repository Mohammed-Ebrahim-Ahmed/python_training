from rps8 import rps
from guess_game import gsgm
import argparse


def aracade_game(name="player"):
    
    choice = ''
    
    while choice != 'x':
        choice = input(f"\n\n{name}, please choice one of the following games\n1 = Rock Paper Scissor\n2 = Guess my Number\nOr press 'x' to exit\n\n")
        
        if(choice == "1"):
            Rock_Paper_Scissor = rps(name)
            Rock_Paper_Scissor()
        elif(choice == "2"):
            Guess_Game = gsgm(name)
            Guess_Game()
        elif(choice.lower() == 'x'):
            print(f"\n{name}, it was fun, please come here again!")
            break
        else:
            print(f"\nWrong choice {name}, please try again")
            aracade_game(name)
    
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="this is the parameters parsed from the aracde game"
    )
    
    parser.add_argument(
        '-n', '--name', metavar="name", required = True, help="The name of the player"
    )
    
    arg = parser.parse_args()
    
    aracade_game(arg.name)
    
    