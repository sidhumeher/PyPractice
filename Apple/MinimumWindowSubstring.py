'''
Created on Oct 27, 2020

@author: sidteegela
'''
from collections import Counter

# Sliding window approach and Brute force approach


def minWindow_bruteforce(s, t):

    s_substrings = []
    
    # All substrings of s
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            s_substrings.append(s[i:j])
    
    t_counter = Counter(t)
    result = []
    
    # Finding substrings that contain t
    for substr in s_substrings:
        s_counter = Counter(substr)
        flag = False
        for item in t_counter:
            if item in s_counter and s_counter[item] >= t_counter[item]:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            result.append(substr)
        s_counter.clear()
        
    # Finding the smallest substring in result list containing t
    
    minWindow = float('inf')
    minWindowString = ''
    
    for substr in result:
        if len(substr) <= minWindow:
            minWindow = len(substr)
            minWindowString = substr
            
    print('Min Window:', minWindow)
    print('Min window string:', minWindowString)

 
def minwindow(s, t):

    # Length of string and pattern
     
    len1 = len(s)
    len2 = len(t)
     
    # check for string and pattern length
    if len1 < len2:
        return
    
    hash_t = [0] * 256  # 256= No of characters
    hash_s = [0] * 256
    
    # Store occurences of pattern t's characters
    for item in t:
        hash_t[ord(item)] += 1
        
    start = 0; start_index = -1; min_length = float('inf')
    count = 0  # count of chars
    
    # character occurences in string
    for item in range(0, len1):
        hash_s[ord(s[item])] += 1
        
        if hash_t[ord(s[item])] != 0 and hash_s[ord(s[item])] <= hash_t[ord(s[item])]:
            count += 1
        
        # If all characters are matched
        if count == len2:
            # Minimize the window
            while hash_s[ord(s[start])] > hash_t[ord(s[start])] or hash_t[ord(s[start])] == 0:
                if hash_s[ord(s[start])] > hash_t[ord(s[start])]:
                    hash_s[ord(s[start])] -= 1
                start += 1

            # Update window size
            len_window = item - start + 1
            if min_length > len_window:
                min_length = len_window
                start_index = start
                
    if start_index == -1:
        return
    
    return s[start_index : start_index + min_length]


# Practice
def minwindow1(s, t):
    
    if len(s) < len(t):
        return
    
    hash_s = [0] * 256
    hash_t = [0] * 256

    for item in t:
        hash_t[ord(item)] += 1
        
    start = 0; minLength = float('inf'); count = 0; startIndex = -1
    
    for i in range(0, len(s)):
        hash_s[ord(s[i])] += 1
        
        if hash_t[ord(s[i])] != 0 and hash_s[ord(s[i])] <= hash_t[ord(s[i])]:
            count += 1
            
        if count == len(t):
            while hash_s[ord(s[start])] > hash_t[ord(s[start])] or hash_t[ord(s[start])] == 0:
                if hash_s[ord(s[start])] > hash_t[ord(s[start])]:
                    hash_s[ord(s[start])] -= 1
                    start += 1

            len_window = i - start + 1
            if minLength > len_window:
                minLength = len_window
                startIndex = start

    if startIndex == -1:
        return
    return s[startIndex:startIndex + minLength]


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    # minWindow_bruteforce(s, t)
    
    s = 'AOBEOCDBAC'
    t = 'ABC'
    # minwindow(s, t)
    print(minwindow1(s, t))
