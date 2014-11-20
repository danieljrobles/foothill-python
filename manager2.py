#In file manager.py
from employee2 import Employee

class Manager(Employee):
    """
    one object of class Manager represents one Manager, which is a subset of
    the class Employee containing all Employee attributes and containing two attributes specific to
    the class Manager: Title and Bonus
    """
    def __init__(self,firstName,lastName,ssn,salary,title, bonus):
        """
        Sets one object of sub-class Manager, using class Employee
        """
        Employee.__init__(self,firstName,lastName,ssn,salary)
        self.title = title
        self.bonus = bonus

    def __str__(self):
        """
        Converts a manager object into a string that lists out the Employee and Manager class attributes
        """
        return (Employee.__str__(self)+ "\n** Manager Properties:\n** Title:.....%s\n** Bonus:.....%s" % (self.title,str(self.bonus)))

if (__name__ == "__main__"):
    #Testing code for testing within the sub-class file
    QA_spacer = "*******************"
    print(QA_spacer)
    print("Testing Manager Subclass of Employee")
    e1 = Manager("Daniel","Manager1","123456789",10000,"sr. mgr.",100)
    e2 = Manager("Daniel","Manager2","123456789",10000,"sr. mgr.",100)
    print(QA_spacer)
    print(e1)
    print(QA_spacer)
    print("Give Raise to Manager: .555 = 55.5%")
    print(QA_spacer)
    e1.giveRaise(.555)
    print(e1)
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
