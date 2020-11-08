'''
Created on Nov 7, 2020

@author: sidteegela
'''
'''
Object oriented programming pillars: 
1. Encapsulation
2. Inheritance
3. Polymorphism

'''


class Customer:
    
    # Constructor/initializer
    def __init__(self, name, membership):  # Overriding init method
        self.name = name
        self.membership = membership
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    def upgrade_membership(self, newMembership):
        self.membership = newMembership

    # Class method. Also called as static method that can be only invoked on a class not object
    # def readCustomer():
    #    print('Reading customer data')
    
    def __str__(self):
        print('Converting customer object')
        return self.name + ',' + self.membership
    
    # Comparing customer objects
    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        else:
            return False


if __name__ == '__main__':
    
    customer1 = Customer('Ann', 'Gold')
    print(customer1.name, customer1.membership)

    # object creation in line
    customers = [Customer('Sid', 'Gold'), Customer('Ann', 'Platinum')]
    print(customers[1].name)
    
    # Print customer
    print(customer1)  # Invokes __str__()
    
    print(customers[0] == customers[1])
