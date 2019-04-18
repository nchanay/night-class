import random

def calc_winner(comp_choice, user_choice):
    defeats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if comp_choice == user_choice:
        return "Tie"
    elif defeats[comp_choice] == user_choice:
        return "Computer wins"
    else:
        return "User wins!"

rps_list = ['rock', 'paper', 'scissors']
while True:
    user_choice = input('Please choose rock, paper, or scissors: ').strip().lower()
    if user_choice in rps_list:
        break
    print("input not valid")
comp_choice = random.choice(rps_list)
print(f"The computer chose {comp_choice}")
print(calc_winner(comp_choice, user_choice))
