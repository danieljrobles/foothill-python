def factorial(n):
    #calculates the factorial of input n.
    ## n = n! = n * (n-1) * (n-2) * (n-3) * … * 1.
    ## The factorial of 0 = 0! = 1.
    f=1
    for x in range(1,n):
        f=f*(x+1)
    return f

for x in range(1,6):
    print(factorial(x))

