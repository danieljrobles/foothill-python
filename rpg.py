"""In file rpg.py
"""
class Hero:
        """One object of class Hero stores one hero's user stats, abilities, ... etc.
        """
        count = 0                       # this is the class variable that counts the number of instances of this class
        heroClasses = {
                # maps a Hero Class single character value to plain English
                "f" : "Fighter",
                "r" : "Ranger",
                "m" : "Mage"
        }
        heroStats = {
                #maps a hero's single character stats value to plain English
                hp : "Health Points",
                mp : "Mana Points",
                st : "Stamina",
                dm : "Damage",
                ap : "Ability Power",
                ar : "Armor",
                mr : "Magic Resist",
                sp : "Speed"
        }

        def __init__ (self):
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
                if self.rank > 9:
                        return "10"
                else:
                        return str(self.rank)

        def __str__(self):
                #Converts a Card object into a string e.g. Ace of Spades, Two of Hearts
                return "%s of %s" % (Card.rankNames[self.rank], Card.suitNames[self.suit],)


#Testing code for testing within the class file
if (__name__ == "__main__"):
        c1 = Card(1,"s")
        print (c1)   # automatcially calls __str__(self) method
