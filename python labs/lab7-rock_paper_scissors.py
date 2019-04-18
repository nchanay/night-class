import random

print("Let's play Rock Paper Scissors!")

rps_list = ['rock', 'paper', 'scissors']

ask_question = "yes"

while ask_question.lower() == "yes":
    comp_choice = random.choice(rps_list)
    user_choice = input(f"What will you choose: {rps_list[0]}, {rps_list[1]}, or {rps_list[2]}?\n> ")
    while user_choice.lower() not in rps_list:
        user_choice = input(f"I'm looking for: ({rps_list[0]}), ({rps_list[1]}), or ({rps_list[2]})\n> ")
    print(f"You have chosen {user_choice}.")
    if user_choice.lower() == "rock":
        if comp_choice == "rock":
            print(f"The computer has chosen {comp_choice}\n-Tie-")
        elif comp_choice == "paper":
            print(f"The computer has chosen {comp_choice}\n-You Lose :( -")
        else:
            print(f"The computer has chosen {comp_choice}\n-You Win!!!-")
    if user_choice.lower() == "paper":
        if comp_choice == "rock":
            print(f"The computer has chosen {comp_choice}\n-You Win!!!-")
        elif comp_choice == "paper":
            print(f"The computer has chosen {comp_choice}\n-Tie-")
        else:
            print(f"The computer has chosen {comp_choice}\n-You Lose :( -")
    if user_choice.lower() == "scissors":
        if comp_choice == "rock":
            print(f"The computer has chosen {comp_choice}\n-You Lose :( -")
        elif comp_choice == "paper":
            print(f"The computer has chosen {comp_choice}\n-You Win!!!-")
        else:
            print(f"The computer has chosen {comp_choice}\n-Tie-")
    ask_question = input("Do you want to play again?\n> ")
    if ask_question.lower() not in ["yes", "no"]:
        ask_question = input("I'm looking for a (yes) or (no)\n> ")

print("Until our next game, Love peace and chicken grease!")
