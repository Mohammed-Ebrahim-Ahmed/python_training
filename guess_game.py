from random import choice

def gsgm(name = "Dave"):
    Game_count = 0
    Player_count = 0
    
    def guess_game():
        nonlocal Game_count
        nonlocal Player_count
        nonlocal name

        player_choice = int(input(f"\n{name}, guess which number I\'m thinking of... 1, 2, or 3.\n"))
        
        if(player_choice not in [1, 2, 3]):
            print(f"\nWrong input number, please {name} enter... 1, 2, or 3 ")
            return guess_game()
        
        computer_choice = int(choice("123"))
        
        print(f"\n{name}, you chose {player_choice}")
        print(f"\nI was thinking about the number {computer_choice}")
        
        def proccess_choices(player, computer):
            nonlocal Player_count
            nonlocal name
            if computer == player:
                Player_count += 1
                return f"\n🎉{name} you win!"
                
            else:
                return "f\n😢 Sorry, {name}... you lose"
        
        print(proccess_choices(player=player_choice, computer=computer_choice))
        Game_count += 1 
        percent = Player_count / Game_count
        
        print(f"\nYour wining percentage: {percent:.2%}")
        

        
        while True:
            print(f"\nPlay again ?, {name}")
        
            player_continue_choice = input("\nY for Yes or\nQ to Quit\n")
            
            if(player_continue_choice.lower() == "y"):
                # do absolutely nothing
                guess_game()
            elif(player_continue_choice.lower() == "q"):
                print(f"\n🎉🎉🎉🎉🎉\n{name}, thanks for playing\nBye {name}")
                break
            else:
                print(f"\nplease, {name} you entered wrong choice, please try again")
                
                
            
    return guess_game
    

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="This is the Guess Game have fun please!"
    )
    
    parser.add_argument(
        "-n", "--name", metavar="name", required="True", help="Enter you name parmeter please"
    )
    
    args = parser.parse_args()
    
    guess_game = gsgm(args.name)
    guess_game()   