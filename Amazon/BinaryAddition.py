'''
Created on Dec 9, 2020

@author: sidteegela
'''


def addBinary(a, b):
    
    if len(a) == 0:
        return bin(b)
    if len(b) == 0:
        return bin(a)
    
    sum = bin(int(a, 2) + int(b, 2))
    return sum


if __name__ == '__main__':
    a = '11'; b = '1'
    print(addBinary(a, b))
    
    a = '1010'; b = '1011'
    print(addBinary(a, b))
