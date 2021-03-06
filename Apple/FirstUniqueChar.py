'''
Created on Nov 4, 2020

@author: sidteegela
'''
from collections import Counter


# Best approach
def firstUniqChar(s):
    
    counter = Counter(s)
    # print(counter)
    for key, value in enumerate(s):
        print(value, counter[value])
        if counter[value] == 1:
            return key
        
    return -1
# Time complexity: O(n)            


if __name__ == '__main__':
    s = "leetcode"
    # s = "loveleetcode"
    # s = ''
    # s = 'cc'
    print(firstUniqChar(s))
