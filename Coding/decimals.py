'''
Created on Jan 7, 2019

@author: siddardha.teegela
'''
from decimal import *

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i >=1:
            positive += 1
        elif i == 0:
            zero += 1
        if i < 0:
            negative += 1
    length = len(arr)
    
    getcontext().prec = 6
    
    print (Decimal(positive)/Decimal(length))
    print (Decimal(negative)/Decimal(length))
    print (Decimal(zero)/Decimal(length))

if __name__ == '__main__':
    arr = [-4,3,-9,0,4,1]
    plusMinus(arr)
