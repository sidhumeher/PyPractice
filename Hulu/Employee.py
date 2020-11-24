'''
Created on Nov 21, 2020

@author: sidteegela
'''

'''
Access modifiers Python
name - Public(Accessible inside and outside of class
_name - Protected (Shouldn't be used outside of class unless subclass)
__name - Private (Only accessible inside class)
'''


class Employee:
    
    empCount = 0  # Class variable
    __hideemp = False  # Data hiding
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        Employee.empCount += 1

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    def del_salary(self):
        del self.__salary
    
    # property() returns the object of property class
    salary = property(get_salary, set_salary, del_salary, "salary's docstring")    
    
    def getCount(self):
        print('Total employees:', Employee.empCount)
        
    # Getter method
    def getNmae(self):
        return self.name
    
    # Setter method
    def setName(self, name):
        self.name = name
        
    def getEmployee(self):
        print('Name:', self.name, ',', 'Salary:', self.salary)
        
    # class method
    @classmethod
    def hello(cls):  # Takes a class argument
        print('hello from', cls.__name__)
        
    # static method
    @staticmethod
    def hello1():
        print('Hello from static method')


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
    
    Employee.hello()  # class method invocation
    emp1.hello()
    
    Employee.hello1()  # static method can be called with class or object
    emp2.hello1()
