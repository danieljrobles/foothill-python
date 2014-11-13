from random import randrange
class Die:
    """
    One object of this class represnts one die with 6 sides. You can roll the die
    to come up with a pseudo random value between 1 and 6.
    """
    def __init__(self):
        """
        Initializes the die to 1.
        """
        self.value = 1

    def __str__(self):
        """
        Returns a string representation of the die.
        """
        return "This die has value : " + str(self.value)

    def roll(self):
        """
        Rolls the die to come up with a pseudorandom value between 1 and 6.
        """
        self.value = randrange(1,7)

