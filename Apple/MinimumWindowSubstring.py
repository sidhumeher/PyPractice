'''
Created on Oct 27, 2020

@author: sidteegela
'''


def minwindow(s, t):

    if len(s) == 0 or len(t) == 0:
        return ''
    elif len(s) < len(t):
        return ''

    no_of_chars = 256
    
    hash_s = [0] * no_of_chars
    hash_t = [0] * no_of_chars

    # store occurences of characters in pattern (t)
    for i in range(0, len(t)):
        hash_t[ord(t[i])] += 1
        
    start = 0; start_index = -1; min_len = float('-inf')
    count = 0  # No of occurences
    
    for j in range(0, len(s)):
        hash_s[ord(s[j])] += 1  # Count occurences of t in s
        
        # If string's char matches with target's char, increment count
        if hash_t[ord(s[j])] != 0 and hash_s[ord(s[j])] <= hash_t[ord(s[j])]:
            count += 1
        
        # If all occurences in s match with t
        if count == len(t):
            # Minimize the window by removing unwanted chars and remove from start
            while hash_t[ord(s[start])] == 0 or hash_s[ord(s[start])] > hash_t[ord(s[start])]:
                if hash_s[ord(s[start])] > hash_t[ord(s[start])]:
                    hash_s[ord(s[start])] -= 1
                
                start += 1
            
            # update window length
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start
                
    # If no window found
    if start_index == -1:
        return ''
    
    print(len(s[start_index:start_index + min_len]))


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    minwindow(s, t)
    
    s = 'AOBEOCDBAC'
    t = 'ABC'
    minwindow(s, t)
