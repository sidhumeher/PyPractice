'''
Created on May 3, 2020

@author: sidteegela
'''

def reverseInteger(inputInt):
    
    sign = -1 if inputInt < 0 else 1
    
    reverse = 0
    inputInt = abs(inputInt)
    
    while inputInt != 0:
        lastDigit = inputInt % 10
        reverse = (reverse * 10) + lastDigit
        inputInt = inputInt//10
        
    if reverse < pow(-2, 31) or reverse > pow(2,31)-1:
        return 0
    else:
        return reverse * sign
        

if __name__ == '__main__':
    
    inputInt = 123
    print(reverseInteger(inputInt))
    
    inputInt = -123
    print(reverseInteger(inputInt))
    
    inputInt = 120
    print(reverseInteger(inputInt))
    
    