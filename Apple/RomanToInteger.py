'''
Created on Nov 8, 2020

@author: sidteegela
'''


def romanToInt(s):
    sum = 0
    roman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            sum -= roman[s[i]]
        else:
            sum += roman[s[i]]
            
    sum += roman[s[-1]]
    return sum
# Time complexity:O(n)
    

if __name__ == '__main__':
    s = 'MCMXCIV'
    print(romanToInt(s))
