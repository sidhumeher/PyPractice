'''
Created on Oct 25, 2020

@author: sidteegela
'''
from collections import defaultdict

# Two strings are anagrams if their sorted strings are equal


def groupAnagrams(strs):
    
    result = defaultdict(list)
    
    # print(tuple(strs[0]))
    # print(tuple(sorted(strs[0])))
    
    for str in strs:
            result[tuple(sorted(str))].append(str) 
            
    print(result.values())
    
# Time Complexity: O(n*k logk), n=no of strings, k=max length of a string in strs
# We iterate through all strings = O(n), we sort each string = O(k logk)
# Space Complexity: O(nk)
    

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(strs)
