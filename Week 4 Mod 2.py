#This is inside a file named "utilityFunctions.py"
""" Returns the result of raising "base" to the power of "exp"
"""
def raiseToPower(base, exp):
    total = 1
    for count in range(exp):    
        total = total * base        
    return total

# here are the two calls to the raiseToPower() function
print ("returned from raiseToPower: %i" % raiseToPower(2,3) )
print ("returned from raiseToPower: %i" % raiseToPower(6,5) )
