'''
Created on Nov 10, 2020

@author: sidteegela
'''

'''
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
We can pass variable no of arguments with special symbols
'''


# Non keyworded arguments with *args
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


# **kwargs allows us to pass keyworded arguments of variable length
# Think of kwargs as a dictionary that maps keywords to values
def myFun2(arg1, **kwargs): 
    print('arg1:', arg1)
    for key, value in kwargs.items():
        print ("%s == %s" % (key, value))


if __name__ == '__main__':
    # *args example
    myFun('Hello', 'Hello', 'World!')
    # myFun('Hello', ['Hello', 'World!'])
    
    # **kwargs example
    myFun2("Hi", first='Hello', mid='World', last='!') 
