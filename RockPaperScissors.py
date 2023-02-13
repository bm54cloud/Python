# Rock, paper, scissors game

import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer): # creating new variables player and computer
    print(f"You chose {player}, the computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Player wins"
    elif player == "paper" and computer == "rock":
        return "Player wins"
    elif player == "scissors" and computer == "paper":
        return "Player wins"
    else:
        return "Computer wins"

choices = get_choices()
# To get the key of a dictionary, do variable = dict_variable["key_name"]
result = check_win(choices["player"], choices["computer"])
print(result)



    


