"""In file card.py
"""
import math

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
                #Check for input errors
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

        def getRank(self):
                #Returns the rank of the card
                return self.rank

        def getSuit(self):
                #Returns the suit of the card
                return self.suit

        def bjValue(self):
                if self.rank > 9:
                        return 10
                else:
                        return self.rank
                
        def __str__(self):
                #Converts a Card object into a string e.g. Ace of Spades, Two of Hearts
                return ("%s of %s" % (Card.rankNames[self.rank], Card.suitNames[self.suit]))

#Testing code for testing within the class file
if (__name__ == "__main__"):
        def printTestCases(r,s):
                #c1 = Card("s",1)
                try:
                        c1 = Card(r,s)
                        print("#################################################")
                        print("#### TESTING: cards.py (rank: %i | suit: %s) #####" % (r,s))
                        print("#################################################")
                        print ("Card(1,'s'):....%s" % c1)   # automatcially calls __str__(self) method
                        print ("getRank():......%s" % c1.getRank())
                        print ("getSuit():......%s" % c1.getSuit())
                        print ("bjValue():......%s" % c1.bjValue())
                        print("##########################\n")
                except ValueError:
                        print ("VALUE ERROR: (%s, %s)" % (str(r),str(s)))
                except TypeError:
                        print ("TYPE ERROR: (%s, %s)" % (str(r),str(s)))
                finally:
                        print("**********************************************")


        #Set the values to test for
        QARanks = [1,14, -1, "s", 1.1]
        QASuits = ["s",1, -1,"spades"]
        combo = []
        for r in QARanks:
                for s in QASuits:
                        combo.append((r,s))
        print(combo)
        for x in combo:
                printTestCases(x[0],x[1])
