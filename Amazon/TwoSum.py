'''
Created on Dec 2, 2020

@author: sidteegela
'''


# Brute Force
def twoSum(nums, target):
    if len(nums) == 0:
        return
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
# Time complexity:O(n^2)
# Space: O(1)


# Optimized
def twoSum1(nums, target):
    if len(nums) == 0:
        return
    
    tracker = {}
    
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in tracker:
            return [tracker[remain], i]
        else:
            tracker[nums[i]] = i

# Time complexity: O(n)
# Space: O(n)
    

if __name__ == '__main__':
    nums = [2, 7, 11, 15]; target = 9
    print(twoSum1(nums, target))

    nums = [3, 2, 4];target = 6
    print(twoSum1(nums, target))

    nums = [3, 3];targer = 6
    print(twoSum1(nums, target))
