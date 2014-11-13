""" One object of this class stores one circle's radius """
class Circle:
    def __init__ (self):
        self.radius = 0

    def setRadius(self, radius):
        self.radius = radius

    def __str__(self):
        return "radius of the circle = %i" % (self.radius)
    

if (__name__ == "__main__"):
    print("*********************")
    print("Testing:.............%s" % __file__)
    print("*********************")
    c = Circle()
    print("print(c):............%s" % c)
    print("print(c.radius):.....%i" % c.radius)
    print("setRadius(10):.......START")
    c.setRadius(10)
    print("setRadius(10):.......END")
    print("print(c.radius):.....%i" % c.radius)
    print("*********************")
