"""Midterm 1
    Rewrite the following block of code in the most efficient way (i.e. fewest comparisons), not knowing anything about the value of income.
    The code that you write must result in the same value for taxRate, given any value for income.
    Assume that the value for income has already been set before entering this block of code.


taxRate = 0
if income >20000 and income <30000:
   taxRate = .15
if income >=30000 and income < 45000:
   taxRate = .20
if income >=45000 and income <75000:
   taxRate = .30
if income >=75000:
   taxrate = .40
"""
#Answer
taxRate = 0
if income >= 75000:
   taxRate = .40
elif income >=45000:
   taxRate = .30
elif income >=30000:
   taxRate = .20
elif income > 20000:
   taxRate = .15
