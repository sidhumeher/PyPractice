'''
Created on Dec 7, 2020

@author: sidteegela
'''


# Using division
def arrayProduct(nums):

    if len(nums) == 0:
        return
    
    product = 1
    for item in nums:
        product *= item
        
    for i in range(len(nums)):
        nums[i] = product // nums[i]
        
    return nums


# Not using division
def arrayProduct1(nums):
    if len(nums) == 0:
        return
    
    left = [1] * len(nums)
    right = [1] * len(nums)

    # Populate left list
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    # Populate right list
    for i in reversed(range(0, len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]
        
    result = [left[item] * right[item] for item in range(len(left))]
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(arrayProduct1(nums))
