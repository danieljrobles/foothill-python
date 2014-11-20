#In file employee_manager_testing.py
"""
This script will test the Employee Class, and the Manager Class (a subclass of Employee)
"""

#IMPORT PY MODULES
from random import randrange

#IMPORT CUSTOM FILES
from manager2 import Manager
from employee2 import Employee

emp1 = Employee("Should Be Last","6","123456789",10000)
emp2 = Employee("Should Be Fifth","5","123456789",10000)
emp3 = Employee("Should Be 3rd 1","4","123456789",10000)
mgr1 = Manager("Should Be 3rd 2 (actually 4th)","4","112346789",100000,"Sr. Mgr.",1000)
mgr2 = Manager("Should Be 2","1","212346789",200000,"Sr. Mgr.",2000)
mgr3 = Manager("Should Be First"," ","212346789",200000,"Sr. Mgr.",2000)
employees = [emp1,emp2,emp3,mgr1,mgr2,mgr3]

for e in employees:
    print("%i|%s %s" % (e.employeeID,e.firstName,e.lastName))


employees = sorted(employees)
print("\n\n")

for e in employees:
    print("%i|%s %s" % (e.employeeID,e.firstName,e.lastName))



#This is an artifact from assignment 7, but because it is not needed for assignment 8 I will simply comment it out.
"""
for e in employees:
    print("******NEW EMPLOYEE*******")
    print(e)
    raisePercent = randrange(100)/100
    print("**********")
    print("GIVE RAISE of %s " % (str(raisePercent)))
    print("**********")
    e.giveRaise(raisePercent)
    print(e)
    print("******END EMPLOYEE*******")
    print("**************************************************")
"""

if (__name__ == "__main__"):
    #Testing code for testing within the __main__ file
    QA_spacer = "*******************"
    print(QA_spacer)
    print ("__doc__="                           + __doc__)
    print(QA_spacer)
    print ("Manager.__doc__="                   + Manager.__doc__)
    print ("Manager.__init__.__doc__="          + Manager.__init__.__doc__)
    print ("Manager.__str__.__doc__="           + Manager.__str__.__doc__)
    print(QA_spacer)
    print ("Employee.__doc__="                  + Employee.__doc__)
    print ("Employee.__init__.__doc__="         + Employee.__init__.__doc__)
    print ("Employee.giveRaise.__doc__="        + Employee.giveRaise.__doc__)
    print ("Employee.printEmpAsRow.__doc__="    + Employee.printEmpAsRow.__doc__)
    print ("Employee.__str__.__doc__="          + Employee.__str__.__doc__)
    print ("Employee.__eq__.__doc__="           + Employee.__eq__.__doc__)
    print ("Employee.__lt__.__doc__="           + Employee.__lt__.__doc__)
