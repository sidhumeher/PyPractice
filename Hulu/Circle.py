'''
Created on Nov 22, 2020

@author: sidteegela
'''
from math import pi


class Circle:
    
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value

    def del_radius(self):
        del self._radius

    radius = property(get_radius, set_radius, del_radius, "radius's docstring")
    
    def getArea(self):
        return (self.get_radius() ** 2) * pi

    
class Cylinder(Circle):  # Inheritance
    
    def __init__(self, radius=1.0, height=1.0):
        super().__init__(radius)  # Calling super class constructor
        self.height = height
        
    def getVolume(self):
        return self.getArea() * self.height  # Inherited getArea()
    
    def __str__(self):
        return 'Cylinder(radius: {},height: {})'.format(self.get_radius(), self.height)
    
    # Override
    def getArea(self):
        return 2.0 * pi * self.radius * self.height  # Surface area of cylinder
        

if __name__ == '__main__':
    
    cy1 = Cylinder(1.1, 2.2)
    print(cy1)
