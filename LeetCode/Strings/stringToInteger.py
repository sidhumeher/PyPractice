'''
Created on May 5, 2020

@author: sidteegela
'''

def myAtoi(s):
    
    if s == ' ':
        return
    s = s.strip()
    s = list(s)
    returnValue = ''
    if s[0].isalpha():
        return 0
        
    if s[0] == '+' or s[0] == '-':
        returnValue += s[0]
        s.pop(0)
    
    for item in s:
        if item.isdigit():
            returnValue += item
        else:
            break
        
    #print('Return:',returnValue)
    returnValue = int(returnValue)     
    if returnValue > pow(-2, 31) and returnValue < pow(2, 31) - 1:
        return int(returnValue)
    else:
        return -2147483648
    
    

if __name__ == '__main__':
    
    s = '42'
    print(myAtoi(s))
    
    s = '-42'
    print(myAtoi(s))
    
    s = '4193 with words'
    print(myAtoi(s))
    
    s = 'words and 987'
    print(myAtoi(s))
    
    s = '-91283472332'
    print(myAtoi(s))
    
    s = '3.14159'
    print(myAtoi(s))
    
    s = '.1'
    print(myAtoi(s))