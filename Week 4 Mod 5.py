""" Returns the factorial or 'number', for 'number' >= 0
"""
def factorial(number):
    if number == 0:
        return 1        # this is called the trivial case
    elif number >1:
        return number * factorial (number -1)  # here is the recursive call
    else:
        return 1
    
#We can now translate this to a Python function definition for factorial(number):

    
for x in range(10):
    print (str(x) + ": " + str(factorial (x)))

