'''
Created on Nov 26, 2020

@author: sidteegela
'''
# Return K most frequent items
from collections import Counter
import heapq


def topKFrequent(nums, k):
    
    if len(nums) == 1:  # O(1) time
        return nums
    
    track = Counter(nums)  # O(n) time
    result = []
    
    # Sorting 1
    # for key in sorted(track, key=track.get, reverse=True):
    #    result.append(key)
    
    # Sorting 2
    for key in sorted(track.items(), key=lambda x:x[1], reverse=True):
        result.append(key[0])
        
    return result[:k]
    
# Time complexity:O(n logn)
# Space: O(k)


# Using heap queue in Python
def topKFrequent1(nums, k):
    
    if len(nums) == 1:  # O(1) time
        return nums
    
    track = Counter(nums)  # O(n) time
    result = []
    
    # Build heapq from top k items in track: O(nlogk) time
    return heapq.nlargest(k, track.keys(), key=track.get)

# Time complexity: O(nlogk) if k < n or O(n) if k==n
# Space: O(n+k), n=size of dictionary,k=size of heap


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]; k = 2
    print(topKFrequent(nums, k))
    
    nums = [1]; k = 1
    print(topKFrequent(nums, k))
    
    nums = [1, 1, 2, 2, 2, 3]; k = 2
    print(topKFrequent1(nums, k))
    
    nums = [3, 0, 1, 0]; k = 1
    print(topKFrequent1(nums, k))
