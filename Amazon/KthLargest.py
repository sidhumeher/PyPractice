'''
Created on Nov 26, 2020

@author: sidteegela
'''
# Find the kth largest element in an unsorted array
import heapq


def findKthLargest(nums, k):
    
    nums.sort(reverse=True)
    print(nums)
    
    return nums[k - 1]

# Time complexity: O(nlogn)
# Space: O(1)


# Using heapq
def findKthLargest1(nums, k):
    
    return heapq.nlargest(k, nums)[-1]  # Returns the last item in heapq

# Time complexity: O(nlogk)
# Space: O(k)
    

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))
    
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))
    
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest1(nums, k))
