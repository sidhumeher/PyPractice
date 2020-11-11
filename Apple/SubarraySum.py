'''
Created on Nov 10, 2020

@author: sidteegela
'''
'''
Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.
'''


# Brute force approach
def subarraySum(nums, k):
    
    count = 0
    
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            sum = 0
            for item in range(i, j + 1):
                sum += nums[item]
                
            if sum == k:
                count += 1
                
    return count
# Time complexity; O(n^3)
# Space: O(1)


# Better approach. Find sum on the fly
def subarraySum1(nums, k):
    
    count = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1

    return count
# Time complexity: O(n^2)
# Space: O(1)


if __name__ == '__main__':
    nums = [1, 1, 1]; k = 2
    print(subarraySum(nums, k))
    
    nums = [1, 2, 3]; k = 3
    print(subarraySum1(nums, k))
