"""
    One object of this class stores one circle's radius. 
    Used in Module 7 to show interface.
    Also is an example of the use of unittest
    In file "circle2.py"
"""

# unittest is a module that contains class TestCase and a main() that will run our test cases.
import unittest

# class Circle is the "unit"
class Circle:
    def __init__ (self):
        self.radius = 0

    def setRadius(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415*(self.radius * self.radius)

    def __str__(self):
       return "Radius of the circle = %i" % (self.radius)

# The rest of this file contains all of our "unit tests"      
class CircleTests (unittest.TestCase):
    def test1(self):
        c = Circle()
        self.assertTrue(c.area() == 0)
        self.assertTrue(str(c) == "Radius of the circle = 0")

    def test2(self):
        c = Circle()
        c.setRadius(1)
        self.assertTrue(c.area() == 3.1415)
        self.assertTrue(str(c) == "Radius of the circle = 1")

    def test3(self):
        c = Circle()
        c.setRadius(-1)
        self.assertFalse(c.area() == -3.1415)
        self.assertFalse(str(c) == "Radius of the circle = 1")

    def test4(self):
        c = Circle()
        c.setRadius(5)
        self.assertTrue(c.area() == 78.53750000000001)
        self.assertTrue(str(c) == "Radius of the circle = 5")

if __name__ == '__main__':
    unittest.main()   # this unittest.main() knows to run every method here whose name starts with "test"
