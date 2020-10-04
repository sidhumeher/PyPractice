'''
Created on Apr 19, 2020

@author: sidteegela
'''

def plusOne(digits):
    
    if digits == []:
        return [1]
    if digits[-1] < 9:
        return digits[:-1]+[digits[-1]+1]
    else:
        return plusOne(digits[:-1]) + [0]
    

if __name__ == '__main__':
    digits = [9]
    result = plusOne(digits)
    print(result)
    
    digits = [1,2,3]
    result = plusOne(digits)
    print(result)