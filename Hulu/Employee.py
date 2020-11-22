'''
Created on Nov 21, 2020

@author: sidteegela
'''


class Employee:
    
    empCount = 0  # Class variable
    __hideemp = False  # Data hiding
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def getCount(self):
        print('Total employees:', Employee.empCount)
        
    def getEmployee(self):
        print('Name:', self.name, ',', 'Salary:', self.salary)


if __name__ == '__main__':
    emp1 = Employee('Ann', 2000)
    emp2 = Employee('Bishop', 4000)
    
    print('Total Employees:', Employee.empCount)

    emp1.getEmployee()
    emp2.getEmployee()
    
    print(getattr(emp1, 'name'))  # getter method
    setattr(emp1, 'salary', 5000)  # setter method
    print(getattr(emp1, 'salary'))
    
    print(hasattr(emp1, 'name'))  # Returns true if salary exists
    
    # print(Employee.__hideemp) #throws AttributeError
    
    # #Data Hiding# #
    # Hidden attributes can be accessed with object._className__attrName
    print(emp1._Employee__hideemp)
