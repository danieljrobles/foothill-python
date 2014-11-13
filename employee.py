#In file employee.py
class Employee:
    """ one object of class Employee represents one Employee with the attributes: Name, Social Security, and Salary
    """
    empCount = 0  #used to maintain the number of employees

    def __init__(self, name, ssn, salary):
        if not name:
            raise ValueError("Name Cannot Be Blank")
        elif len(str(ssn)) != 9:
            raise ValueError("Social Security Must Be Nine Digits.  You entered %s" % (len(str(ssn))))
        else:
            self.name = name
            self.ssn = ssn
            self.salary = salary
            Employee.empCount += 1
            self.employeeID = Employee.empCount

    def giveRaise(self,percentRaise):
        #this function will modify an employee's base salary by:
        #  taking in the parameter percentRaise adding one to it, then multiplying by the base salary
        percentRaise = float(percentRaise)
        self.salary = (self.salary*(1+percentRaise))

    def __str__(self):
        #Converts an Employee object into a string that lists out the Employee class attributes
        return ("********************\nEmployee Properties:\nEmp #:.....%i\nName:......%s\nSocial:....%s\nSalary:....%s" % (self.employeeID,self.name,self.ssn,self.salary))

if (__name__ == "__main__"):
    #Testing code for testing within the class file
    QA_spacer = "*******************"
    print(QA_spacer)
    print("Testing Employee")
    print(QA_spacer)
    print("Create objects")
    e1 = Employee("Daniel1","123456789",10000)
    e2 = Employee("Daniel2","023456789",10000)
    print(QA_spacer)
    print("Print Employee Objects:")
    print(e1)
    print(e2)
    print(QA_spacer)
    print("Give Raises:\n Employee 1 Raise: '.15'\n Employee 2 Raise: '.25'")
    e1.giveRaise(.15)
    e2.giveRaise(.25)
    print(QA_spacer)
    print("Print Employee Objects:")
    print(e1)
    print(e2)
    
