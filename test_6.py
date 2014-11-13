userInput = input ("Please type a real number: ")

try:
    float_userInput = float(userInput)
    print("Thank you for following instructions.")
    print("I hope you play again.")
except:
    print("You typed a char that isn't appropriate in a real number.")
    print("I hope you play again.")

"""
try:
    deck[totalCards] = card2.Card(rank,suit)
    totalCards = totalCards+1
except ValueError as specificErrorObject:
    print ("****************\n* VALUE ERROR\n* INPUT:............(%s, %s)\n* ERROR MESSAGE:....%s\n****************" % (str(rank),str(suit),str(specificErrorObject.args[0])))
except TypeError as specificErrorObject:
    print ("****************\n* TYPE ERROR\n* INPUT:............(%s, %s)\n* ERROR MESSAGE:....%s\n****************" % (str(rank),str(suit),str(specificErrorObject.args[0])))




if type(rank) != int:
        raise TypeError("Rank value (%s) not an interger" % str(rank))
elif type(suit) != str:
        raise TypeError("Suit value (%s) must be a string in the set ('d','c','h','s')"  % str(suit))
elif rank <1 or rank > 13:
        raise ValueError("Rank value (%s) outside of range [1, 13]"  % str(rank))
elif suit not in ("d","c","h","s"):
        raise ValueError("Suit value (%s) not in character set ('d','c','h','s')"  % str(suit))
#If not errors are found, then build the card
else:
        self.rank = rank
        self.suit = suit
        Card.count = Card.count + 1
"""
