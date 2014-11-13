"""In file card.py
"""
#QA: print(__name__)
class Card:
        """One object of class Card stores one card's rank and suit
        """
        count = 0                       # this is the class variable that counts the number of instances of this class
        suitNames = {
                # maps a suits single character value to plain English
                "d" : "Diamonds",
                "c" : "Clubs",
                "h" : "Hearts",
                "s" : "Spades"
        }
        rankNames = {
                #maps a card's single character rank value to plain English
                1 : "Ace",
                2 : "Two",
                3 : "Three",
                4 : "Four",
                5 : "Five",
                6 : "Six",
                7 : "Seven",
                8 : "Eight",
                9 : "Nine",
                10 : "Ten",
                11 : "Jack",
                12 : "Queen",
                13 : "King"
        }

        def __init__ (self,rank,suit):
                #Card constructor, executed every time a new Card object is created
                self.rank = rank
                self.suit = suit
                #self.area = self.getArea()
                Card.count = Card.count + 1

        def getRank(self):
                #Returns the rank of the card
                return self.rank

        def getSuit(self):
                #Returns the suit of the card
                return self.suit

        def bjValue(self):
                #Returns the blackjack value of the card
                if self.rank > 9:
                        return 10
                else:
                        return self.rank

        def __str__(self):
                #Converts a Card object into a string e.g. Ace of Spades, Two of Hearts
                return "%s of %s" % (Card.rankNames[self.rank], Card.suitNames[self.suit],)


#Testing code for testing within the class file
if (__name__ == "__main__"):
        c1 = Card(1,"s")
        print (c1)   # automatcially calls __str__(self) method
