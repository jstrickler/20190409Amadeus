#!/usr/bin/env python
import random

class CardDeck: # object
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer_name):
        self.dealer_name = dealer_name
        self._cards = None
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def get_dealer_name(self):
        return self._dealer_name

    @property
    def dealer_name(self):
        return self._dealer_name

    @dealer_name.setter
    def dealer_name(self, dealer_name):
        if isinstance(dealer_name, str):
            self._dealer_name = dealer_name
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def bark():
        return "Woof! Woof!"

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return '{}({})'.format(
            my_name, len(self)
        )

    def __add__(self, other):
        tmp = type(self)(self.dealer_name)
        tmp._cards = self.cards + other.cards
        return tmp

