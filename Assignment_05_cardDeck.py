"""This script to create 52 Card objects and print the names of those cards in plain English
"""
import card

#Set the range of values for a 52 card deck
ranks = range(0,13)
suits = ("d", "c", "h", "s")

#initialize an empty deck dictionary
deck = {}
totalCards = 1

#loop through the ranges to fill the deck with card objects
for suit in suits:
    for rank in ranks:
        deck[totalCards] = card.Card(rank+1,suit)
        totalCards = totalCards+1

#print the deck with the card number, plain english rank and suit, and the blackjack value
for c in deck:
    print("%i: %s has Blackjack Value of: %i" % (c,deck[c],deck[c].bjValue()))
