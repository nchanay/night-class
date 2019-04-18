"""
#  deck.py
Card and Deck classes
"""
from random import shuffle as rand_shuf


class Card:
    """
    Card represented by suit and rank
    """

    def __init__(self, rank, suit):
        ace = {'A', 1}
        nums = dict(zip(range(2, 11), range(2, 11)))
        face = {k: 10 for k in 'JQK'}
        points.update(nums)
        points.update(face)

        self.rank = rank
        self.suit = suit
        self.points = points

    def __repr__(self):
        return f'Card: [{self.rank} of {self.suit}]'

    def __eq__(self, card):
        return self.rank == card.rank

    def __ne__(self, card):
        return self.rank != card.rank

    def __add__(self, card):
        pass


class Deck:
    """
    Deck as a list of card
    """

    def __init__(self):
        ranks = ['A'] + list(range(2, 11)) + list('JQK')
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __repr__(self):
        cards = ''
        for card in self.cards:
            cards += str(card) + '\n'
        return cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def shuffle(self):
        """
        Shuffles cards in place
        """
        rand_shuf(self.cards)

    def cut(self, index):
        """
        Cuts the deck at index
        """
        index %= 52
        self.cards = self.cards[index:] + self.cards[:index]

    def draw(self):
        """
        Pops card off top of deck
        """
        return self.cards.pop()
