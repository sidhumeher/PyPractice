'''
Created on Oct 8, 2020

@author: sidteegela
'''

'''
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: [0,0]
Output: [0,0]
'''

'''
A two-pointer approach could be helpful here. The idea would be to have one pointer 
for iterating the array and another pointer that just works on the non-zero elements 
of the array.
'''


def moveZeroes(nums):
    p = 0
    nonZ = 0
    while nonZ < len(nums):
        if nums[nonZ] != 0:
            nums[p], nums[nonZ] = nums[nonZ], nums[p]
            p += 1
        nonZ += 1
    print(nums)


if __name__ == '__main__':
    pass
