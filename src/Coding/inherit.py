'''
Created on Dec 27, 2018

@author: siddardha.teegela
'''
class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    
    def Name(self):
        return self.firstname+" "+self.lastname

class Employee(Person):
    def __init__(self,first,last,no):
        Person.__init__(self, first, last)
        '''
        super().__init__(first,last) in python3
        super(Employee,self).__init__(first,last,no) compatible with python 2,3
        '''
        self.number = no
        
    def getEmployee(self):
        return self.Name()+" "+ self.number

if __name__ == '__main__':
    x = Person("Candy","Paulsen")
    y = Employee("Jim","Paulsen","1001")
    
    print(x.Name())
    print(y.getEmployee())