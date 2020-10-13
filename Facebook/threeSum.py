'''
Created on Oct 11, 2020

@author: sidteegela
'''


def threeSum(nums):
    
    def helper(num1, num2):
        return num1 + num2
        
    if len(nums) == 0 or nums == [0]:
        return []
    
    result = []
    i, j = 0, 0
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums) - 2):
            if nums[i] + helper(nums[j], nums[j + 1]) == 0:
                result.append([nums[i], nums[j], nums[j + 1]])
    
    print(result)


if __name__ == '__main__':
    
    nums = [-1, 0, 1, 2, -1, -4]
    threeSum(nums)
