'''
Created on May 4, 2020

@author: sidteegela
'''
from collections import Counter

def firstUniqChar(s):

    count = Counter(s)
    outputIndex = -1 
    
    for alphabet in s:
        if count[alphabet] == 1:
            return s.index(alphabet)
        
    return outputIndex
    

if __name__ == '__main__':
    
    s = 'leetcode' 
    print(firstUniqChar(s))
    
    s = 'loveleetcode'
    print(firstUniqChar(s))