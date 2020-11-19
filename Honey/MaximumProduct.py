'''
Created on Nov 17, 2020

@author: sidteegela
'''
'''
Given an integer array. Find 3 numbers whose product is maximum and output the maximum product

Ex: [1,2,3,4] output: 24

Assumptions:
No duplicates
Not sorted array or no sorting allowed
'''


# Does not work for negative items in list
def maxProduct(nums):
    
    if len(nums) == 0:
        return 0

    first = second = third = float('-inf')
    
    for item in nums:
        
        if item > first:
            third = second
            second = first
            first = item
        elif item < first and item > second:
            third = second
            second = item
        elif item < second and item > third:
            third = item
            
    product = first * second * third
    return product

# Time complexity: O(n)
# space complexity: O(1)


def maxProduct1(nums):
    
    if len(nums) == 0:
        return 0
    
    min1 = float('inf'); min2 = float('inf')
    max1 = float('-inf'); max2 = float('-inf'); max3 = float('-inf')

    for item in nums:
        # If item is between min1 and min2
        if item <= min1:
            min2 = min1
            min1 = item
        elif item <= min2:
            min2 = item
        # If item lies in range max1,max2,max3 or higher
        if item >= max1:
            max3 = max2
            max2 = max1
            max1 = item
        elif item >= max2:
            max3 = max2
            max2 = item
        elif item >= max3:
            max3 = item
        
    product = max(min1 * min2 * max1, max1 * max2 * max3)
    return product
# Time complexity: O(1)
# Space: O(1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(maxProduct(nums))
    
    nums = [1, 2, 3, 4]
    print(maxProduct(nums))
    
    nums = [2, 4, 3, 1]
    print(maxProduct(nums))
    
    nums = [2, 4, 3, 1, -4, -5]
    print(maxProduct1(nums))
    
    nums = [-1, -2, -3]
    print(maxProduct1(nums))
    
    nums = [0, 0, 0]
    print(maxProduct1(nums))
