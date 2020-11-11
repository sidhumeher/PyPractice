'''
Created on Nov 4, 2020

@author: sidteegela
'''


def missingNumber(nums):
    
    if len(nums) == 0:
        return 
    
    for index in range(len(nums) + 1):
        if index not in nums:
            return index
# Time complexity: O(n^2)


def missingNumber_optimized(nums):
    
    if len(nums) == 0:
        return 
    
    nums.sort()  # Time: O(n) or O(log n) based on algorithm
    
    # Edge cases. First item must be 0 and last item must be length of nums
    if nums[0] != 0:
        return 0
    elif nums[-1] != len(nums):
        return len(nums)
    
    currentNum = 0
    
    for item in nums:
        if item != currentNum:
            return currentNum
        currentNum += 1

# Time compelxity: O(nlogn)


if __name__ == '__main__':
    # nums = [0]
    # nums = [3, 0, 1]
    # nums = [0, 1]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber_optimized(nums))
    
