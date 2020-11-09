'''
Created on Nov 8, 2020

@author: sidteegela
'''


def lengthOfLongestSubstring(s):
    
    if len(s) == 0:
        return 0
    
    tracker = {}
    left = 0; right = 0
    maxlength = 0
    
    while right < len(s):
        if right not in tracker:
            tracker[s[right]] = 1
            maxlength = max(maxlength, len(tracker))
            right += 1
        else:
            del tracker[s[left]]
            left += 1
            
    return maxlength
# Time complexity; O(n)
# Space: len(s) worst case


if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
