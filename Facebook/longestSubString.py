'''
Created on Oct 8, 2020

@author: sidteegela
'''

# find the length of the longest substring without repeating characters.

# Sliding window method
# If a duplicate is not found add to dictionary and move right, if found remove it from dictionary and move
# left pointer to right size


def longestSubString(s):

    if s == "":
        return 0
      
    alpha = dict()
    left = 0
    right = 0
    maxLength = 0
        
    while right < len(s):
        if s[right] not in alpha:
            alpha[s[right]] = 1
            maxLength = max(maxLength, len(alpha))
            right += 1     
        else:
            del alpha[s[left]]
            left += 1
            
    return maxLength


if __name__ == '__main__':
    pass
