"""This script will create 52 Card objects and print the names of those cards in plain English.
    The script will also pass values outside of the acceptable range for a card including:
    -- strings for integer parameters
    -- integers for string parameters
    -- floats for integer parameters
    -- floats for string parameters
    -- integers outside of the card rank range
    -- strings that are not in the acceptable set of strings
"""
import card2

#Set the range of values for a 52 card deck
ranks = list(range(0,14))
ranks.append(1.1)
ranks.append("s")
suits = ("d", "c", "h", "s","e",1,1.1)

print(ranks)

#initialize an empty deck dictionary
deck = {}
totalCards = 0

#loop through the ranges to fill the deck with card objects
for suit in suits:
    for rank in ranks:
        try:
            deck[totalCards] = card2.Card(rank,suit)
            totalCards = totalCards+1
        except ValueError as specificErrorObject:
            print ("****************\n* VALUE ERROR\n* INPUT:............(%s, %s)\n* ERROR MESSAGE:....%s\n****************" % (str(rank),str(suit),str(specificErrorObject.args[0])))
        except TypeError as specificErrorObject:
            print ("****************\n* TYPE ERROR\n* INPUT:............(%s, %s)\n* ERROR MESSAGE:....%s\n****************" % (str(rank),str(suit),str(specificErrorObject.args[0])))

#print the deck with the card number, plain english rank and suit, and the blackjack value
for c in deck:
    print("%i: %s has Blackjack Value of: %i" % (c+1,deck[c],deck[c].bjValue()))

