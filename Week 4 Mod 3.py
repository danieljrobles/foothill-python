""" Multiplies 'number' by 2, but this change is not reflected in the calling code
"""
def double (number):
    number = number *2

# here is the main part of the program containing the function call
num = 2
double (num)
print (num)

""" appends a 4 to the end of 'list'
"""
def addTo(list):
    list.append(4)

# here is the main part of the program containing the function call
list = [1,2,3]
addTo(list)  # list is changed by this function call
print (list)  

#However, if we try to make list point to a different list, this will not be reflected back in the main part of the program:

""" makes 'list' point to a list that has an additional element in it
"""
def addTo(list):
    list = list + [4]

# here is the main part of the program with the function call
list = [1,2,3]
addTo(list)
print (list)    # now list is unchanged by this function call

