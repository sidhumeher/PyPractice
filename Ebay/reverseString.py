'''
Created on Oct 5, 2020

@author: sidteegela
'''

'''
Interview question:
Reverse a string leaving special characters as they are 

Input: a,b$c
Output: c,b$a

Assumption: No numbers in the inputstring
'''


def reverse(inputString):
    
    leftPointer = 0
    rightPointer = len(inputString) - 1
    
    inputString_to_list = list(inputString)

    while leftPointer < len(inputString_to_list) - 1 and rightPointer > -1:
        if inputString_to_list[leftPointer].isalpha() and inputString_to_list[rightPointer].isalpha():
            inputString_to_list[leftPointer], inputString_to_list[rightPointer] = inputString_to_list[rightPointer], inputString_to_list[leftPointer]
            leftPointer += 1
            rightPointer -= 1
        elif inputString_to_list[leftPointer].isalpha() != True:
            leftPointer += 1
        elif inputString_to_list[rightPointer].isalpha() != True:
            rightPointer -= 1
        
    # return str(inputString_to_list)
    return ''.join(inputString_to_list)


if __name__ == '__main__':
    
    input = 'a,b$c'
    result = reverse(input)
    print(result)
    
    input = 'p@as$w0rd'
    result = reverse(input)
    print(result)
