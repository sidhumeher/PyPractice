'''
Created on Nov 17, 2020

@author: sidteegela
'''


# Converting to string and then integer and adding
def digitsSum(num):
    
    if 0 <= num <= 9:
        return num

    totalsum = 0
    for digit in str(num):
        totalsum += int(digit)
        
    return totalsum


# Using mod operation
def digitsSum1(num):
    
    totalSum = 0

    while num != 0:
        num, remain = divmod(num, 10)
        totalSum += remain
    return totalSum


if __name__ == '__main__':
    num = 678
    print(digitsSum(num))
    
    num = 123
    print(digitsSum1(num))
