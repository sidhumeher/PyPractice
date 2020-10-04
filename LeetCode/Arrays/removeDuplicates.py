'''
Created on Mar 28, 2020

@author: sidteegela
'''


def removeDuplicates(nums):
    
    if len(nums) == 0:
            return len(nums)
    
    alreadyPresent = nums[0]
    currentIndex = 1
        
    while currentIndex < len(nums):
        if nums[currentIndex] == alreadyPresent:
            nums.pop(currentIndex)
        else:
            alreadyPresent = nums[currentIndex]
            currentIndex += 1
    #print(nums)
    return len(nums)
                

if __name__ == '__main__':
    print('Case1')
    nums = [1,1,2]
    
    length = removeDuplicates(nums)
    print(nums)
        
    print('Case2')
    nums = [0,0,1,1,1,2,2,3,3,4]
    
    length = removeDuplicates(nums)
    print(nums)
    