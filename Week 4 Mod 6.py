"""lambda is a special way to define a function.
A lambda is an expression that represents a function that returns a value.
A lambda expression does not have to have a name like a function does, but
it can take parameters just like a function can.
Here is an addTax function written as a function and then as a lambda expression:
"""
def addTax(price):
    return price + price * 0.0825

print (addTax(10))         # call the function "addTax"

addTax = lambda price: price + price * 0.0825 # redefine the name "addTax"

print (addTax(10))    # call the lambda expression "addTax"

print("######################################################")

functionList = [lambda x: x+x , lambda x: x*x, lambda x: x**x]

# we can call an individual lambda in this list on the argument 10 with the following code:

print ( functionList[1](10) )

# or we can call all the lambdas in this list on the argument 5 with the following loop:

 

for index in range(3):

     print ("functionList[%i](5)= %i"  %  (index, functionList[index](5)) )
