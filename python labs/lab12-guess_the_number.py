# guess the number
import random

def hottercolder (cg, pg):
    if abs(cg) < abs(pg):
        print("You're getting hotter!")
    elif abs(cg) > abs(pg):
        print("You're getting colder..")
    else:
        print("Your guess neither hotter nor colder.")

computers_choice = random.randint(1, 100)
print("The Computer has randomly selected a number between 1 and 100")

attempt = 0
past_guess = 0
while True:
    while True:
        current_guess = input("What is your guess?\n> ")
        if current_guess.isdigit():
            current_guess = int(current_guess)
            break
        else:
            print("Please enter a number")
    if current_guess == computers_choice:
        print(f"By golly you got it!\nIt took you {attempt} attempts")
        break
    elif current_guess < computers_choice:
        print("Looks a little on the low side")
        if attempt > 0:
            hottercolder(current_guess, past_guess)
        past_guess = current_guess
        attempt = attempt + 1
    elif current_guess > computers_choice:
        print("You're aiming too high, bring it down a bit")
        if attempt > 0:
            hottercolder(current_guess, past_guess)
        past_guess = current_guess
        attempt = attempt + 1
