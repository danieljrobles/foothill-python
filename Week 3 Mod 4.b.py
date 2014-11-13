""" generates a random number between 1 and 10, and asks the user to guess what it is
"""

import random  # needed to use randint()
secretNumber = random.randint(1,10)

userInput = input("Pick a number between 1 and 10: ")
userGuess = int (userInput)
while userGuess != secretNumber:
    if userGuess < secretNumber:
        print ("The Number is greater")
    else:
        print ("The Number is smaller")
    userInput = input("Pick a number between 1 and 10: ")
    userGuess = int (userInput)
if userGuess == secretNumber:
     print("You got it!")

