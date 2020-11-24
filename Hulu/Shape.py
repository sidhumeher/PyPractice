'''
Created on Nov 22, 2020

@author: sidteegela
'''
from math import pi


class Shape:
    
    def __init__(self, color='Red'):
        self.color = color
        
    def __str__(self):
        return 'Shape(color={})'.format(self.color)
    
    __repr__ = __str__
    
    
class Circle(Shape):
    
    def __init__(self, radius=1.0, color='Red'):
        super().__init__(color)
        self.radius = radius
        
    def __str__(self):
        return 'Circle({}, radius={})'.format(super().__str__(), self.radius)
    
    __repr__ = __str__
    
    def getArea(self):
        return (self.radius ** 2) * pi


class Rectangle(Shape):
    
    def __init__(self, length=1.0, width=1.0, color='Red'):
        super().__init__(color)
        self.length = length
        self.width = width
        
    def __str__(self):
        return 'Rectangle({}, length={}, height={})'.format(super().__str__(), self.length, self.width)
    
    __repr__ = __str__

    def getArea(self):
        return self.length * self.width
    
    
class Square(Rectangle):
    
    def __init__(self, side=1.0, color='Red'):
        super().__init__(side, side, color)
        
    def __str__(self):
        return 'Square({})'.format(super().__str__())
    

if __name__ == '__main__':
    
    s1 = Shape('Teal')
    print(s1)
    print(repr(s1))
    
    c1 = Circle(1.8, 'Blue')
    print(c1)
    print(c1.getArea())
    
    r1 = Rectangle(1.2, 2.3, 'Green')
    print(r1)
    print(r1.getArea())
    
    s1 = Square(2.0, 'White')
    print(s1)
    
