'''
Created on Nov 22, 2020

@author: sidteegela
'''
from abc import abstractmethod


class A:
    
    def __init__(self):
        print('Init A')
    
    def testmethod(self):
        print('Testmethod of class A')
    
    @abstractmethod
    def testmethod1(self):  # Abstract method has no implementation and so cannot be called
        pass
        
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print('Init B')
    
    def testmethod(self):
        print('Testmethod of class B')

        
class C(A):        
    
    def __init__(self):
        super().__init__()
        print('Init C')
    
    def testmethod(self):
        print('Testmethod of class C')


class D(B, C):
    
    def __init__(self):
        super().__init__()
        print('Init D')

        
# Multiple inheritance        
class D1(B, C):
    
    def __init__(self):
        pass

    
class D2(C, B):
    
    def __init__(self):
        pass

    
class D3(B, C):
    
    def __init__(self):
        pass
    
    # Overridden method
    def testmethod(self):
        print('Testmethod of class D3')


if __name__ == '__main__':

    d1 = D1()
    d1.testmethod()

    d2 = D2()
    d2.testmethod()
    
    d3 = D3()
    d3.testmethod()
    
    d = D()
    # MRO- Method Resolution Order
    print(D.mro())
    print(B.mro())
    print(C.mro())
