'''
Created on Nov 9, 2020

@author: sidteegela
'''

# OOP: Multiple Inheritance
'''
Every class in Python is derived from Object class. It is the most base type in Python

'''


class Base1:
    pass


class Base2:
    pass


class Base3(Base1, Base2):
    pass  # Derives features from classes Base1 and Base2 and itself

# Multi-level Inheritance

'''
In the below example, class search order is [Derived2, Derived1, Base, object] class
This order is called linearization and the rules used to find this class is called
Method Resolution Order (MRO)
MRO ensures that a class always appears before its parents. 
In case of multiple parents, the order is the same as tuples of base classes.
'''


class Base:
    pass


class Derived1(Base):
    pass  # Derives features from Base class and itself


class Derived2(Derived1):
    pass  # Derives features from Base and Derived1 classes and itself


if __name__ == '__main__':
    pass
