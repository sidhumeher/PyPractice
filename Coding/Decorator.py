'''
Created on Nov 9, 2020

@author: sidteegela
'''

'''
Decorator:
A decorator takes in a function, adds some functionality to it and returns it
This is called metaprogramming as a part of program tries to modify another part of 
program at compile time
'''


def make_pretty(func):
    
    def inner():
        print('I got decorated')
        func()

    return inner


# We can use '@' to decorate a function
@make_pretty
def ordinary():
    print('This method is ordinary')


def smart_divide(func):  # Decorator function with parameters
    
    def inner(a, b):
        print('Dividing a with b')
        if b == 0:
            print('Divide with zero.Exiting')
            return
        
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


if __name__ == '__main__':
    
    # Exmaple1
    
    # ordinary()
    # Decorators demonstration
    pretty = make_pretty(ordinary)  # make_pretty() is a decorator
    pretty()
    
    # Another way to call decorator with '@' above
    # ordinary = make_pretty(ordinary)
    ordinary()
    
    # Exmaple2- With parameter
    
    divide(2, 4)
    divide(5, 0)
