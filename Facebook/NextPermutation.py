'''
Created on Oct 14, 2020

@author: sidteegela
'''


def nextPermutation(nums):
    
    if len(nums) == 1:
        return nums

    i = len(nums) - 1
    j = len(nums) - 1
    
    # Finding that index where i-1 is less than i
    while i > 0 and nums[i - 1] > nums[i]:
        i -= 1
    if i == 0:  # If the number is highest possible then no next permutation is possible.Return lowest
        return nums.reverse()
    
    k = i - 1
    # Find that number j, big enough to swap with i-1
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[k], nums[j]
    
    left = k + 1
    right = len(nums) - 1
    # Reverse the part of nums after k to get next permutation
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1 
        right -= 1
        
# Time Complexity: O(n)
# Space: O(1)


if __name__ == '__main__':
    pass
