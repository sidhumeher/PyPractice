'''
Created on Oct 11, 2020

@author: sidteegela
'''


def romanToInteger(s):
    
    roman_to_integer = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    
    for i in range(len(s) - 1):
        # print(i)
        if roman_to_integer[s[i]] < roman_to_integer[s[i + 1]]:
            sum -= roman_to_integer[s[i]]
        else:
            sum += roman_to_integer[s[i]]
        print(sum)
    
    print(sum + roman_to_integer[s[-1]])


if __name__ == '__main__':

    s = 'III'
    # romanToInteger(s)
    s = 'LVIII'
    # romanToInteger(s)
    s = 'MCMXCIV'
    romanToInteger(s)
