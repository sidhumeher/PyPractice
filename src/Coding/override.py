'''
Created on Dec 27, 2018

@author: siddardha.teegela
'''

class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname+" "+self.lastname
    
class Employee(Person):
    def __init__(self,first,last,no):
        self.number = no
        super().__init__(first, last)
    
    def __str__(self):
        return super().__str__()+", "+str(self.number)

if __name__ == '__main__':
    x = Person("Candy","Paulsen")
    y = Employee("Jim","Paulsen",1001)
    
    print(x)
    print(y)