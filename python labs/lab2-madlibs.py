#this code was from my intro course, but I have added lists and commented out old code that I have changed

# The quote “Through dangers untold and hardships unnumbered I have fought my way here to the castle beyond the Goblin City to take back the child you have stolen, for my will is as strong as yours and my kingdom as great. You have no power over me!”
import random

ask_question = input("Do you want to try my madlib? yes or no\n>")
while True:
    while ask_question.lower() not in ["yes", "no"]:
        ask_question = input("I'm looking for a (yes) or (no)\n>")
    if ask_question.lower() == "yes":
        noun_list = []
        ploural_noun_list = []
        verb_list = []
        # mad_dangers = input("Give me a plural noun: ")
        ploural_noun_list.append(input("Give me a plural noun: "))
        # mad_hardships = input("Give me another plural noun: ")
        ploural_noun_list.append(input("Give me another plural noun: "))
        # mad_fought = input("Give me past tense verb: ")
        verb_list.append(input("Give me past tense verb: "))
        mad_castle = input("Give me a building type: ")
        mad_goblin = input("Give me a creature: ")
        # mad_child = input("Give me a noun: ")
        noun_list.append(input("Give me a noun: "))
        # mad_stolen = input("Give me past tense verb: ")
        verb_list.append(input("Give me past tense verb: "))
        # mad_will = input("Give me a noun: ")
        noun_list.append(input("Give me a noun: "))
        # mad_kingdom = input("Give me a noun: ")
        noun_list.append(input("Give me a noun: "))
        # mad_power = input("Give me a noun: ")
        noun_list.append(input("Give me a noun: "))

        random.shuffle(noun_list)
        random.shuffle(ploural_noun_list)
        random.shuffle(verb_list)

        # print(f"Through {mad_dangers} untold and {mad_hardships} unnumbered I have {mad_fought} my way here to the {mad_castle} beyond the {mad_goblin} City to take back the {mad_child} you have {mad_stolen}, for my {mad_will} is as strong as yours and my {mad_kingdom} as great. You have no {mad_power} over me!")
        print(f"Through {ploural_noun_list[0]} untold and {ploural_noun_list[1]} unnumbered I have {verb_list[0]} my way here to the {mad_castle} beyond the {mad_goblin} City to take back the {noun_list[0]} you have {verb_list[1]}, for my {noun_list[1]} is as strong as yours and my {noun_list[2]} as great. You have no {noun_list[3]} over me!")

        ask_question = input("Do you want to try again?\n>")
    if ask_question.lower() == "no":
        print("Aww, well you're no fun.")
        break
