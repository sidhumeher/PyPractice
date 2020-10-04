'''
Created on Apr 13, 2020

@author: sidteegela
'''

def containsDuplicate(nums):
    
    if len(nums) == 0:
        return False 
    
    nums.sort()
    
    visitedItem = nums[0]
    
    for i in range(1,len(nums)):
        if visitedItem == nums[i]:
            return True
        else:
            visitedItem = nums[i]
            i += 1
        
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    
    result = containsDuplicate(nums)
    print(result)
    
    nums = [1,2,3,4]
    
    result = containsDuplicate(nums)
    print(result)
    
    nums = [1,1,1,3,3,4,3,2,4,2]
    
    result = containsDuplicate(nums)
    print(result)
    