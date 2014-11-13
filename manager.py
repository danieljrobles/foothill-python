#In file manager.py
from employee import Employee

class Manager(Employee):
    """ one object of class Manager represents one Manager, which is a subset of
    the class Employee containing all Employee attributes and containing two attributes specific to
    the class Manager: Title and Bonus
    """
    def __init__(self, name,ssn,salary,title, bonus):
        Employee.__init__(self, name,ssn,salary)
        self.title = title
        self.bonus = bonus

    def __str__(self):
        #Converts a manager object into a string that lists out the Employee and Manager class attributes
        return (Employee.__str__(self)+ "\n** Manager Properties:\n** Title:.....%s\n** Bonus:.....%s" % (self.title,str(self.bonus)))

if (__name__ == "__main__"):
    QA_spacer = "*******************"
    print(QA_spacer)
    print("Testing Manager Subclass of Employee")
    e1 = Manager("Daniel","001122334",1000,"sr. mgr.",100)
    print(QA_spacer)
    print(e1)
    print(QA_spacer)
    print("Give Raise to Manager: .555 = 55.5%")
    e1.giveRaise(.555)
    print(e1)
