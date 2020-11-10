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


if __name__ == '__main__':
    myFun('Hello', 'Hello', 'World!')
    # myFun('Hello', ['Hello', 'World!'])
