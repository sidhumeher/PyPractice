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


if __name__ == '__main__':
    # nums = [0]
    # nums = [3, 0, 1]
    # nums = [0, 1]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums))
    
