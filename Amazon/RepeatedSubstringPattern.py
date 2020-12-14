'''
Created on Dec 10, 2020

@author: sidteegela
'''


def repeatedSubstringPattern(s) -> bool:
        
        tracker = {}
        
        for item in s:
            if item not in tracker:
                tracker[item] = 1
            else:
                tracker[item] += 1
                
        index = 0
        values = list(tracker.values())
        while index < len(values):
            if values[index] != values[index - 1]:
                return False
            index += 1
        return True
    
# Time complexity: O(n)
# Space: O(n)


if __name__ == '__main__':
    s = 'abab'
    print(repeatedSubstringPattern(s))
    
    s = 'aba'
    print(repeatedSubstringPattern(s))
    
    s = 'abcabcabcabc'
    print(repeatedSubstringPattern(s))
