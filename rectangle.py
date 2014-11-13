#In file rectangle.py

class Rectangle:
        count = 0                 # this is the class variable

        #One object of  class Rectangle stores one rectangle's length and width
        def __init__ (self):
                #Rectangle constructor, executed every time a new Rectangle object is created
                print ('constructing a Rectangle object')
                self.height = 0
                self.width = 0
                self.area = self.getArea()
                Rectangle.count = Rectangle.count + 1

        def setData(self, newHeight, newWidth):
                #Sets the height and width inside the Rectangle object
                self.height = newHeight
                self.width = newWidth
                self.area = self.getArea()

        def __str__(self):
                #Converts a Rectangle object into a string 
                return "height = %i, and width = %i, and area: %i" % (self.height, self.width, self.area)

        def getArea(self):
                return (self.height * self.width)
                

""" 
Since the following code is not indented, it is not part of the
class Rectangle. This code is used for testing objects of class
Rectangle. This code creates two Rectangle objects and calls
methods on them for testing purposes. We call this the test program.
"""

if (__name__ == "__main__"):
        r1 = Rectangle()
        print (r1)   # automatcially calls __str__(self) method
        # and prints the returned value
        r1.setData(3,4)
        print (r1)

        r2 = Rectangle()
        r2.setData(5,6)
        print (r2)

        print (Rectangle.count)
        r = Rectangle()
        print (Rectangle.count)
        r = Rectangle()
        print (Rectangle.count)
        r = Rectangle()
        print (Rectangle.count)


