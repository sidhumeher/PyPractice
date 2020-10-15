'''
Created on Oct 13, 2020

@author: sidteegela
'''

# Letter Combinations of a Phone Number

pairing = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
               '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'],
               '9':['w', 'x', 'y', 'z']}


def letterCombinations(digits):
    
    resultArray = []
    
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return pairing[digits[0]]
   
    def helper(letterCombination, nextDigits):
        
        if len(nextDigits) == 0:
            resultArray.append(letterCombination)
        else:
            for letter in pairing[nextDigits[0]]:
                print(letterCombination + letter)
                helper(letterCombination + letter, nextDigits[1:])

    helper('', digits)
    return resultArray

# Time Complexity: O(3^n * 4^m), n=No of digits with 3 letter, m= No of digits with 4letters
# Space Complexity: O(3^n * 4^m) to store those no of solutions


if __name__ == '__main__':
    
    # print(letterCombinations('2'))
    print(letterCombinations('23'))
    # print(letterCombinations('234'))
    
    # print(['a', 'b', 'c'] + ['d', 'e', 'f'])
