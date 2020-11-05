'''
Created on Nov 3, 2020

@author: sidteegela
'''


def letterCombinations(digits):
        
    combinations = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
                    '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                    '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        
    result = []
        
    def helper(current, remaining):
            
        if len(remaining) == 0:
            result.append(current)
            return
        else:
            for char in combinations[remaining[0]]:
                helper(current + char, remaining[1:])
        
    if len(digits) == 0:
        return []
    else:
        helper("", digits)
        return result

# Time Complexity: O(3^n * 4^m), n=Digits with 3 letters, m=Digits with 4 letters
# Space Complexity: O(3^n * 4^m)


if __name__ == '__main__':
    digits = '23'
    
    print(letterCombinations(digits))
