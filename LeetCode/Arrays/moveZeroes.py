'''
Created on Apr 19, 2020

@author: sidteegela
'''

def moveZeroes(nums):
    
    slow = 0 
    fast = 0
    
    while fast < len(nums):
        if nums[slow] == 0 and fast != 0:
            nums[slow],nums[fast] = nums[fast],nums[slow]
            
        if nums[slow] != 0:
            slow += 1
            
        fast += 1
    

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)
    
    nums = [0,0,1]
    moveZeroes(nums)
    print(nums)
   