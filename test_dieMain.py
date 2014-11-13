"""This script will:
    Create two objects of class Die
    Roll them both 10 times.
    After each roll, print the value of both dice so you can examine the output and see how many pairs you rolled.
"""
import die

d1 = die.Die()
d2 = die.Die()

for rollNum in range(1,11):
    d1.roll()
    d2.roll()
    print("Roll: %i | %s | %s" % (rollNum,d1,d2))
