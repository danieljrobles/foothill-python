#In file employee.py
from functools import total_ordering

@total_ordering
class Employee:
    """
    one object of class Employee represents one Employee with the attributes: Name, Social Security, and Salary
    """
    empCount = 0  #used to maintain the number of employees

    def __init__(self, firstName, lastName, ssn, salary):
        """
        Sets one object of class Employee
        """
        if not firstName:
            raise ValueError("First Name Cannot Be Blank")
        elif not lastName:
            raise ValueError("Last Name Cannot Be Blank")
        elif len(str(ssn)) != 9:
            raise ValueError("Social Security Must Be Nine Digits.  You entered %s" % (len(str(ssn))))
        else:
            self.firstName      = firstName.lower()
            self.lastName       = lastName.lower()
            self.ssn            = ssn
            self.salary         = float(salary)
            
            Employee.empCount   += 1
            self.employeeID     = Employee.empCount

    def giveRaise(self,percentRaise):
        """
        this function will modify an employee's base salary by
        taking in the parameter percentRaise adding one to it, then multiplying by the base salary
        """
        percentRaise = float(percentRaise)
        self.salary = (self.salary*(1+percentRaise))

    def printEmpAsRow(self):
        """
        this function will print out the Employee object attributes in a 'table' formatted row
        """
        print("%5i\t%-16s\t%-16s\t%12s\t%12s" % (self.employeeID,self.firstName,self.lastName,self.ssn,self.salary))

    def __str__(self):
        """
        Converts an Employee object into a string that lists out the Employee class attributes
        """
        return ("Emp#:....%i\nName:....%s %s\nSocial:..%s\nSalary:..%s" % (self.employeeID,self.firstName,self.lastName,self.ssn,self.salary))

    def __eq__(self, other):
        """
        Returns True if self == other, False otherwise
        """
        return self.firstName==other.firstName and self.lastName==other.lastName

    def __lt__(self, other):
        """
        Return True when the name in self is alphabetically less than the name in other.
        If the last names are equal, then checks the first names to determine which object is less than the other.
        This must be dictionary ordering, aka "case insensitive" --> this was managed by forcing all firstName
        and lastName values to be entered as lowercase.  It can also be done within __lt__ by referencing a lower here.
        """
        if self.lastName<other.lastName:
            return True
        elif self.lastName > other.lastName:
            return False
        else:  # last names are equal, then check first names
            return self.firstName < other.firstName  

if (__name__ == "__main__"):
    #Testing code for testing within the class file
    QA_spacer = "*******************"
    
    e1 = Employee("Daniel0","Robles","123456789",10000)
    print(QA_spacer)
    print(e1)
    print(QA_spacer)
    e2 = Employee("Daniel1","Robles","123456789",10000)
    e3 = Employee("Daniel1","Robles","123456789",10000)
    employees = [e1,e2,e3]
    print("Employees:")
    print("%5s\t%-16s\t%-16s\t%12s\t%12s" % ("ID","First Name","Last Name","SSN","Salary"))
    for e in employees:
        e.printEmpAsRow()
    print(QA_spacer)
    print("Give Raises:\n Employee 1 Raise: '.15'\n Employee 2 Raise: '.25'")
    print(QA_spacer)
    e1.giveRaise(.15)
    e2.giveRaise(.25)
    print("%-5s\t%-16s\t%-12s\t%-12s" % ("ID","Name","SSN","Salary"))
    for e in employees:
        e.printEmpAsRow()
    print(QA_spacer)
    print ("e1 == e2:..%s" % str(e1 == e2))
    print ("e1 < e2:...%s" % str(e1 < e2))
    print ("e1 > e2:...%s" % str(e1 > e2))
    print(QA_spacer)
    print ("Employee.__doc__="                  + Employee.__doc__)
    print ("Employee.__init__.__doc__="         + Employee.__init__.__doc__)
    print ("Employee.giveRaise.__doc__="        + Employee.giveRaise.__doc__)
    print ("Employee.printEmpAsRow.__doc__="    + Employee.printEmpAsRow.__doc__)
    print ("Employee.__str__.__doc__="          + Employee.__str__.__doc__)
    print ("Employee.__eq__.__doc__="           + Employee.__eq__.__doc__)
    print ("Employee.__lt__.__doc__="           + Employee.__lt__.__doc__)

