'''
Created on Dec 7, 2020

@author: sidteegela
'''
# String to integer conversion


def atoi(s):
    
    if len(s) == 0:
        return None
    
    if s[0].isalpha():
        return 0

    s.strip()  # Removing leading  and trailing whitespaces
    parsedString = ''
    
    for item in s:
        if item.isnumeric() or item == '-' or item == '+':
            parsedString += item
            
    parsedString = int(parsedString)
    
    if parsedString > pow(2, 31):
        return pow(2, 31)
    elif parsedString < pow(-2, 31):
        return pow(-2, 31)
    else:
        return parsedString
    
# Time complexity: O(n)
# Space: O(1)    
    

if __name__ == '__main__':
    s = "42"
    print(atoi(s))
    
    s = 'words and 987'
    print(atoi(s))
    
    s = '4193 with words'
    print(atoi(s))
