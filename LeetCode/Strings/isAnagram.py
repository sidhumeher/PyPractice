'''
Created on May 5, 2020

@author: sidteegela
'''
from collections import Counter

def isAnagram(s, t):
    
    counter_s = Counter(s)
    counter_t = Counter(t)
    check1 = True
    check2 = True
    
    for alphabet in s:
        if counter_s[alphabet] != counter_t[alphabet]:
            check1 = False
    
    for alphabet in t:
        if counter_t[alphabet] != counter_s[alphabet]:
            check2 = False
    
    if check1 != False and check2 != False:
        return True
    else:
        return False


# Run time: 64ms
# Space 14.2 MB

if __name__ == '__main__':
    
    s = 'anagram'
    t = 'nagaram'
    print(isAnagram(s, t))
    
    s = 'rat'
    t = 'cat'
    print(isAnagram(s, t))
    
    s = 'a'
    t = 'ab'
    print(isAnagram(s, t))