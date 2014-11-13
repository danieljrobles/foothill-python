#Week 4: Functions and their Arguements
import random
cycleString = input('Number of Cycles: ')
cycle = int(cycleString)
n1 = 0
n2 = 1
line = ''
for i in range(0,cycle):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    for j in range(0,n3):
        line = line + "#"
    line = line+"\n"
print (line)
    
