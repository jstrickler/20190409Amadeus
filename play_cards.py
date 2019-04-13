#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

# CardDeck d1 = new CardDeck("Flo")

d1 = CardDeck("Flo")
d2 = CardDeck("Eddie")

print(d1)

# BAD PRACTICE:
# print(d1._dealer_name)

print(d1.get_dealer_name())

print(d1.dealer_name)

d1.dealer_name = 'Emily'
print(d1.dealer_name)

try:
    d1.dealer_name = 1.2
except TypeError as err:
    print(err)


print(d1.cards, '\n')
d1.shuffle()
print(d1.cards, '\n')
# CardDeck.shuffle(d1)
d2.shuffle()

print(d1.get_ranks(), '\n')

print(CardDeck.get_ranks())

print(CardDeck.RANKS)

print(CardDeck.bark())

print(d1, d2)
print(d1.draw())
print(len(d1))

# len(d1)
# CardDeck.__len__(d1)
d3 = d1 + d2
print(d3)
print(d3.draw())

j1 = JokerDeck("Fred")
j1.shuffle()
print(j1.draw())
print(j1)
print(j1.cards)
