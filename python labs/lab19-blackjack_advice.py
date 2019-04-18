# Blackjack Advice
from random import choice

playing_cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
# playing_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def deal(num):
    """
    Deals a variable number of cards at random from the playing_cards dictionary
    """
    return [choice(list(playing_cards.keys())) for i in range(num)]


def points(cards):
    """
    Detrmines the total point value of your current cards
    Reduces Ace's point value from 11 to 1 if total points over 21
    """
    points = 0
    count = 0
    for card in cards:
        points += playing_cards[card]
        if card == 'A':
            count += 1

    while count > 0:
        if points > 21:
            points -= 10
            count -= 1
        else:
            break

    return points


def advice(points):
    """
    Provides advice based on points, or lets you know if you have Blackjack or Busted
    """
    if points < 17:
        return "hit"
    elif points >= 17 and points < 21:
        return "stay"
    elif points == 21:
        return "Blackjack!"
    else:
        return "Busted"


def hit(hand):
    """
    Adds 1 random card to your hand
    """
    hand += deal(1)
    return hand


comp_hand = deal(2)
redeal = True
while redeal:
    if points(comp_hand) > 20:
        comp_hand = deal(2)
    else:
        redeal = False

hand = deal(2)
redeal = True
while redeal:
    if points(hand) > 20:
        hand = deal(2)
    else:
        redeal = False

print("\n" + "Welcome to blackjack!")
print(f"The dealer's hand is {comp_hand}, and is worth {points(comp_hand)}")
print('='*60)
print(f"To start we have delt you 2 cards. Your hand is : {hand}")
print(f"Your hand is worth {points(hand)} points, our advice is to : {advice(points(hand))}")

valid_inputs = ["h", "hit", "s", "stay"]
user_choice = advice(points(hand))
loop = True
while user_choice in valid_inputs:
    print('='*60)
    while loop:
        user_choice = input("Would you like to do? (Hit) or (Stay)\n: ").lower().strip()
        if user_choice not in valid_inputs:
            print("Invlad input")
        else:
            break
    if user_choice in ['h', 'hit']:
        hand = hit(hand)
        print(f"your new hand is {hand}, and is worth {points(hand)}")
        print(f"Our advice is to : {advice(points(hand))}")
        if advice(points(hand)) == "Blackjack!":
            print("Oh dang you won! Game Over")
            user_choice = "Game Over"
            loop = False
        elif advice(points(hand)) == "Busted":
            print("Ohhh no! You done busted :( Game Over!")
            user_choice = "Game Over"
            loop = False
    else:
        break


while points(hand) < 22 and advice(points(hand)) in valid_inputs:
    print(f"The computer's hand is {comp_hand} and is worth {points(comp_hand)} points")
    if points(comp_hand) < points(hand):
        print("The computer hits")
        comp_hand = hit(comp_hand)
    elif points(comp_hand) > points(hand) and points(comp_hand) < 21:
        print(f"The computer wins {points(comp_hand)} to {points(hand)}")
        break
    elif points(comp_hand) == 21:
        print(f"The computer wins: BlackJack!")
        break
    elif points(comp_hand) > 21:
        print(f"The computer loses: Busted!")
        break
    elif points(comp_hand) == points(hand):
        print(f"It's a tie! computer wins {points(comp_hand)} to {points(hand)}")
        break
    else:
        print(f"You win {points(hand)} to {points(comp_hand)}")
        break
