'''
Created on May 3, 2020

@author: sidteegela
'''


def reverseString(inputString):
    
    # With inbuilt function reverse()
    # inputString.reverse()

    # Without using inbuilt functions
    inputString[:] = inputString[::-1]


def reverseWithRecursion(inputString):
    
    if len(inputString) == 0:
        return inputString
    
    return reverseWithRecursion(inputString[1:]) + inputString[0]


if __name__ == '__main__':
    
    inputString = ["h", "e", "l", "l", "o"]
    reverseString(inputString)
    print(inputString)
    
    inputString = ["H", "a", "n", "n", "a", "h"]
    reverseString(inputString)
    print(inputString)
    
    print(reverseWithRecursion('Siddardha'))
