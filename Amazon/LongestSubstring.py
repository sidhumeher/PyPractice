'''
Created on Dec 2, 2020

@author: sidteegela
'''

# Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s):

    if len(s) == 0:
        return 0
    
    maxLength = float('-inf')
    tracker = []
    index = 0
    
    while index < len(s):
        if s[index] not in tracker:
            tracker.append(s[index])
            maxLength = max(maxLength, len(tracker))
        elif s[index] in tracker:
            tracker.pop(0)
        index += 1
            
    return maxLength

# Time complexity: O(n)
# Space: O(n), worst case


if __name__ == '__main__':
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))
    
    s = 'bbbbb'
    print(lengthOfLongestSubstring(s))
    
    s = 'pwwkew'
    print(lengthOfLongestSubstring(s))
    
    s = ''
    print(lengthOfLongestSubstring(s))
