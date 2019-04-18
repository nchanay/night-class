print("Welcome to the magic 8-ball! May the furtunes ever be in your favor")

import random

predictions = ["It is certain", "It is decidedly so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not to tell you", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

ask_question = input("Do you want to ask the Magic 8-Ball a question? (yes) or (no)\n> ")

condition = True

while condition:
    while ask_question.lower() not in ["yes", "no", "done"]:
        ask_question = input("I'm looking for a (yes) or (no/done)\n> ")
    if ask_question.lower() == "yes":
        user_question = input("What question do you dare ask the Magic 8-Ball!?\n> ")
        print("...\n...\n...")
        print(f"You have asked {user_question}; the Magic 8-Ball says: {random.choice(predictions)}.")
        ask_question = input("Do you want to try again? or are you done?\n> ")
    if ask_question.lower() == "done" or "no":
        print("Not everyone is ready for answers")
        condition = False
