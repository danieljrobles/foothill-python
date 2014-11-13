""" In file rectangle.py. One object of  class Rectangle stores one
    rectangle's length and width.
"""
class Rectangle:
    def setData(self, newHeight, newWidth):
        self.height = newHeight
        self.width = newWidth

"""  the __str__( ) method is used to convert a Rectangle object
            into a string
"""
def __str__(self):
    return "height = %i, width = %i" % (self.height, self.width)

"""
   Since the following code is not indented, it is not part of the
   class Rectangle. This code is used for testing objects of class
   Rectangle. This code creates two Rectangle objects and calls
   methods on them for testing purposes. We call this the test program.
"""
r1 = Rectangle()
r1.setData(3,4)
print (r1)   # automatcially calls __str__(self) method and prints the returned value
r2 = Rectangle()
r2.setData(5,6)
print (r2)
print (__str__(r1))
print (__str__(r2))

