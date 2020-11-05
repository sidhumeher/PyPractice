'''
Created on Nov 3, 2020

@author: sidteegela
'''
from collections import Counter


def majorityElement(nums):  # Brute force and extra space
    if len(nums) == 0:
        return []
    
    # majority = abs(len(nums) / 3)
    majority = len(nums) // 3
    occurences = Counter(nums)
    result = []
    
    for key, value in occurences.items():
        if value > majority:
            result.append(key)
            
    return result
# Time: O(n+m), n= No of items in nums, m=No of items greater than majority
# Space: O(n+m), n= No of items in dictionary, m=size of results[]

# Technique: Boyer-Moore Voting Algorithm
'''
There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.
and so on
'''


def majorityElement_bestapproach(nums):
    
    if len(nums) == 0:
        return []

    # 1st pass
    count1, count2, candidate1, candidate2 = 0, 0, None, None
    # O(n) time
    for n in nums:
        if candidate1 == n:
            count1 += 1
        elif candidate2 == n:
            count2 += 1
        elif count1 == 0:
            candidate1 = n
            count1 += 1
        elif count2 == 0:
            candidate2 = n
            count2 += 1
        else:
            count1 -= 1; count2 -= 1
    # O(n) time
    # 2nd pass
    result = []
    for item in [candidate1, candidate2]:
        if nums.count(item) > len(nums) // 3:
            result.append(item)
            
    return result
# Time complexity: O(n)+O(n) = O(n)
# Space: O(1)


if __name__ == '__main__':
    nums = [3, 2, 3]
    # print(majorityElement(nums))
    print(majorityElement_bestapproach(nums))
    
    nums = [1]
    # print(majorityElement(nums))
    print(majorityElement_bestapproach(nums))
    
    nums = [1, 2]
    # print(majorityElement(nums))
    print(majorityElement_bestapproach(nums))
    
