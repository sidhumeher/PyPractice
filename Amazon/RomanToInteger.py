'''
Created on Dec 7, 2020

@author: sidteegela
'''


def romantoInteger(s):
    
    if len(s) == 0:
        return None
    
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    
    for i in range(len(s) - 1):
        if mapping[s[i]] < mapping[s[i + 1]]:
            result -= mapping[s[i]]
        else:
            result += mapping[s[i]]
            
    result += mapping[s[-1]]            
    return result

# Time complexity: O(n)
# Space:O(1)


if __name__ == '__main__':
    s = "III"
    print(romantoInteger(s))
    s = 'LVIII'
    print(romantoInteger(s))
    s = 'MCMXCIV'
    print(romantoInteger(s))
