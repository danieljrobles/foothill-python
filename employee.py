#In file employee.py
from functools import total_ordering

@total_ordering
class Employee:
    """ one object of class Employee represents one Employee with the attributes: Name, Social Security, and Salary
    """
    empCount = 0  #used to maintain the number of employees

    def __init__(self, firstName, lastName, ssn, salary):
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
            self.salary         = salary
            
            Employee.empCount   += 1
            self.employeeID     = Employee.empCount

    def giveRaise(self,percentRaise):
        """this function will modify an employee's base salary by
           taking in the parameter percentRaise adding one to it, then multiplying by the base salary
        """
        percentRaise = float(percentRaise)
        self.salary = (self.salary*(1+percentRaise))

    def printEmployee_asRow(self):
        """this function will print out the Employee object attributes in a 'table' formatted row
        """
        print("%5i\t%-16s\t%-16s\t%12s\t%12s" % (self.employeeID,self.firstName,self.lastName,self.ssn,self.salary))

    def __str__(self):
        """Converts an Employee object into a string that lists out the Employee class attributes
        """
        return ("Emp#:....%i\nName:....%s %s\nSocial:..%s\nSalary:..%s" % (self.employeeID,self.firstName,self.lastName,self.ssn,self.salary))

    def __eq__(self, other):
        """Returns True if self == other, False otherwise
        """
        return self.firstName==other.firstName and self.lastName==other.lastName

    def __lt__(self, other):
        """Returns True if self == other, False otherwise
        """
        if self.lastName<other.lastName:
            return True
        elif self.lastName > other.lastName:
            return False
        else:  # last names are equal, then check first names
            return self.firstName < other.firstName  

if (__name__ == "__main__"):
    #Testing code for testing within the class file
    e1 = Employee("Daniel0","Robles","123456789",10000)
    print(e1)
    e2 = Employee("Daniel1","Robles","123456789",10000)
    e3 = Employee("Daniel1","Robles","123456789",10000)
    employees = [e1,e2,e3]
    print("Employees:")
    print("%5s\t%-16s\t%-16s\t%12s\t%12s" % ("ID","First Name","Last Name","SSN","Salary"))
    for e in employees:
        e.printEmployee_asRow()
    print("Give Raises:\n Employee 1 Raise: '.15'\n Employee 2 Raise: '.25'")
    e1.giveRaise(.15)
    e2.giveRaise(.25)
    print("%-5s\t%-16s\t%-12s\t%-12s" % ("ID","Name","SSN","Salary"))
    for e in employees:
        e.printEmployee_asRow()
    
    print ("e1 == e2:..%s" % str(e1 == e2))
    print ("e1 < e2:...%s" % str(e1 < e2))
    print ("e1 > e2:...%s" % str(e1 > e2))


