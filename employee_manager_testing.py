#In file employee_manager_testing.py
#This script will test the Employee Class, and the Manager Class (a subclass of Employee)

#IMPORT PY MODULES
from random import randrange

#IMPORT CUSTOM FILES
from manager import Manager
from employee import Employee

emp1 = Employee("Daniel1, Not A Manager","012346789",100000)
emp2 = Employee("Daniel2, Not A Manager","022346789",200000)
mgr1 = Manager("Daniel M1, A Manager","112346789",100000,"Sr. Mgr.",1000)
mgr2 = Manager("Daniel M2, A Manager","212346789",200000,"Sr. Mgr.",2000)
employees = [emp1,emp2,mgr1,mgr2]

for e in employees:
    print("******NEW EMPLOYEE*******")
    print(e)
    raisePercent = randrange(100)/100
    print("GIVE RAISE of %s " % (str(raisePercent)))
    e.giveRaise(raisePercent)
    print(e)
