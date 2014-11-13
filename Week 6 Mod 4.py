""" Sets the values of the instance variables height and width,
    assuming they are both positive.
"""
def setData(self, height, width):
    if height <0 or width <0:
        raise ValueError()
    self.height = height
    self.width = width
