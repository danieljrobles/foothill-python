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
                if newHeight <0 or newWidth <0:
                        raise ValueError()
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
        def testCases (x,y):
                print("###############################")
                print("H: %i | W: %i" % (r[0],r[1]))
                r1 = Rectangle()
                try:
                    r1.setData(x,y)
                except:
                    print ("can't set the Rectangle to a negative value")
                print (r1)
                print("###############################\n")
        
        rectangles = ((-1,-1),(-1,1),(1,-1),(1,1))
                
        for r in rectangles:
                testCases(r[0],r[1])
                     
        
