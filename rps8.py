import sys
import random
from enum import Enum

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter...\n1 for Rock,\n2 for paper,or \n3 for scissors:\n\n"
        )
        if int(playerchoice) not in [1, 2, 3]:
            print(f"{name}, You must enter 1, 2 or 3.")
            return play_rps()

        player = RPS(int(playerchoice))
        computer_choice = random.choice("123")
        computer = RPS(int(computer_choice))

        print(f"You choose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        def decide_winner(player, computer):
            
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            
            if player == RPS.ROCK and computer == RPS.SCISSORS:
                player_wins += 1
                return f"😍 {name}, You win!"
                
            elif player == RPS.PAPER and computer == RPS.ROCK:
                player_wins += 1
                return f"😍 {name}, You win!"
                
            elif player == RPS.SCISSORS and computer == RPS.PAPER:
                player_wins += 1
                return f"😍 {name}, You win!"
                
            elif player == computer:
                return "🤫 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!, Sorry {name} 😥 ..."
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame Count: {game_count}")
        print(f"\n{name} Count: {player_wins}")
        print(f"\nPython Count: {python_wins}")
        print(f"\nPlay again, {name}?")

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
            print(f"\n Thank you, {name}")
            # Exit the game
            # sys.exit(f"\nBye, {name}! 😪")
            
    return play_rps




if __name__ == "__main__":

    
    import argparse

    parser = argparse.ArgumentParser(
        description= "provide a personl greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person for personalized experience."
    )
    
    args = parser.parse_args()  
    rock_paper_scissors = rps(args.name)   
    rock_paper_scissors() 