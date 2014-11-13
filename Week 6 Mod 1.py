import random

def numberGuess(userInput):
    print("########################\nGuess: %s" % userInput)
    try:
        number = int (userInput)
        print("success")
    except:
        print("in the except clause")
    else:
        print("in the else clause")
    finally:
        print ("in the finally clause\n########################\n")


secretNumber = random.randint(1,10)

print("########################\n## SECRET: %s ###########\n########################\n" % secretNumber)

#userInput = input ("Pick a number ")
userInput = (1,secretNumber,'a')

for x in userInput:
    numberGuess(x)
