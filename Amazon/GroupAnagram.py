'''
Created on Dec 7, 2020

@author: sidteegela
'''
from _collections import defaultdict


def groupAnagrams(strs):
    
    if len(strs) == 0:
        return [[""]]
    
    tracker = defaultdict(list)
    
    for item in strs:
            tracker[tuple(sorted(item))].append(item)
            
    print(tracker)
    return list(tracker.values())

# Time complexity:O(n)
# Space: O(n)


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
