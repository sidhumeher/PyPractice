'''
Created on Nov 10, 2020

@author: sidteegela
'''

# Types of methods: Instance methods, Class methods. Static methods


class MyClass(object):

    def method(self):
        return 'instance method called', self

    # Class method can only access the class and modify class state
    # That change applies to all objects of class
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # Do not accept a class or object as parameter, but can take other parameters
    @staticmethod
    def staticmethod():
        return 'static method called'


if __name__ == '__main__':
    myObj = MyClass()
    # Instance method
    print(myObj.method())
    # Class method
    print(myObj.classmethod())
    # Static method
    print(myObj.staticmethod())
    
    # Without creating an instance
    print(MyClass.classmethod())

    print(MyClass.staticmethod())
    
    print(MyClass.method())  # Must throw error since we did not create object
