'''
Created on Dec 7, 2020

@author: sidteegela
'''


# Using sort
def missingNumber(nums):
    
    if len(nums) == 0:
        return None
    
    nums.sort()
    
    # Checking edge cases, first and last index
    if nums[0] != 0:
        return 0
    if len(nums) != nums[-1]:
        return len(nums)    
    
    # Missing number must be somewhere between 0 and len(nums)
    
    for item in range(1, len(nums)):
        expected = nums[item - 1] + 1
        if expected != nums[item]:
            return expected
    
# Time complexity:O(nlogn)
# Space:O(1)


# Using set
def missingNumber1(nums):
    
    missing = set(nums)
    
    for item in range(0, len(nums) + 1):
        if item not in missing:
            return item

# Time complexity:O(n)
# Space: O(n)


if __name__ == '__main__':
    nums = []
