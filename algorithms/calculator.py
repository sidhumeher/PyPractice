'''
Created on Apr 11, 2019

@author: siddardha.teegela
'''

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ == '__main__':
    print('Enter Input:')
    inputStr = input()
    
    breakInputStr = inputStr.split(' ')
    totalResult = 0
    
    