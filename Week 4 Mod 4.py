""" prints 'number' copies of 'symbol'
"""
def printChars(number, symbol = '*'):
      print (symbol * number)


print("should print 10 asterisks: ")
printChars (10)       # should print 10 asterisks
printChars (10, '$')  # should print 10 dollar signs

#And in fact, both of the function calls above will work with the function definition below:


""" prints 'number' copies of 'symbol'
"""
def printChars(number=10, symbol = '*'):
      print (symbol * number)

printChars(1)  # causes runtime error
