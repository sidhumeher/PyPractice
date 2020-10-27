'''
Created on Oct 23, 2020

@author: sidteegela
'''
'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
'''


# Linear search
def searchRange(nums, target):

    if len(nums) == 0:
        return [-1, -1]
    
    first = -1; last = -1

    for index, item in enumerate(nums):
        if item == target and first == -1:
            first = index
        # print(index)
        if item == target:
            last = index
        # last = index
    print(first, last)
        
    return [first, last]
# Time complexity: O(n)

# Binary search O(log n) time


def serchRange_Binarysearch(nums, target):
    
    def firstOccurence(nums, target):
    
        low = 0; high = len(nums) - 1
        result = -1
    
        while(low <= high):
            mid = (high + low) // 2
            
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                # If target is mid, then we move to left half
                result = mid
                high = mid - 1
        return result
    
    def lastOccurence(nums, target):
        
        low = 0; high = len(nums) - 1
        result = -1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                # If mid is target, then move the right half
                result = mid
                low = mid + 1
        return result

    print([firstOccurence(nums, target), lastOccurence(nums, target)])
    
    return [firstOccurence(nums, target), lastOccurence(nums, target)]
            

if __name__ == '__main__':
    nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    target = 5
    searchRange(nums, target)
    
    nums = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 8
    serchRange_Binarysearch(nums, target)
    
