'''
Created on Nov 3, 2020

@author: sidteegela
'''


def productExceptSelf(nums):
    if len(nums) == 0:
        return []
    
    product = 1
    for item in nums:
        product *= item
        
    result = [product // item for item in nums]
    return result

# Time complexity: O(n)
# Space complexity: O(n)

    
# Without division
# Using Left and Right list to store product
def productExceptSelf_usingList(nums):
    
    left = [1] * len(nums)
    right = [1] * len(nums)
    
    result = []
    
    index = 0
    while index < len(nums) - 1:
        left[index + 1] = nums[index] * left[index]
        index += 1
    
    index = len(nums) - 1
    while index > 0:
        right[index - 1] = nums[index] * right[index]
        index -= 1
        
    index = 0
    for index in range(len(nums)):
        result.append(left[index] * right[index])
    
    return result

# Time complexity: O(n)
# Space: O(n)


# No additional lists used
def productExceptSelf_withoutextraspace(nums):

    if len(nums) == 0:
        return []

    result = [0] * len(nums)
    result[0] = 1  # No items to the left of index 0
    
    for i in range(1, len(nums)):
        result[i] = nums[i - 1] * result[i - 1]
        
    r = 1  # Contains product of all items to the right of index
    for i in reversed(range(len(nums))):
        result[i] = result[i] * r
        r *= nums[i]
        
    return result

# Time complexity: O(n)
# Space: O(1), excluding space for result list


# Practice
def productExceptSelf_usingList1(nums):
    
    if len(nums) == 0:
        return []

    result = []
    left = [1] * len(nums)
    right = [1] * len(nums)
    
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]
    
    for i in reversed(range(0, len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]
        
    for i in range(len(left)):
        result.append(left[i] * right[i])
        
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # print(productExceptSelf(nums))
    
    nums = [4, 5, 1, 8, 2]
    print(productExceptSelf_usingList(nums))
    
    print(productExceptSelf_withoutextraspace(nums))
