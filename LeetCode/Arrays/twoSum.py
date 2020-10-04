'''
Created on Apr 20, 2020

@author: sidteegela
'''

def twoSum(nums,target):
    result = []
    '''
    for i in range(len(nums)-1):
        for j in range(1,len(nums)-1):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    ''' 
    '''
    for i in range(len(nums)):
        reminder = target - nums[i]
        if reminder in nums[:i-1]:
            #print(i)
            #print(nums.index(reminder,0,i-1))
            result.append(i)
            result.append(nums.index(reminder,0,i-1))
        elif reminder in nums[i+1:]:
            #print(i)
            #print(nums.index(reminder,i+1,len(nums)-1))
            result.append(i)
            result.append(reminder,i+1,len(nums)-1)
    '''     
    
    my_dict = dict()
    
    for item in range(len(nums)):
        reminder = target - nums[item]
        if reminder in my_dict:
            result.append(item)
            #print(item)
            result.append(my_dict[reminder])
            #print(my_dict[reminder])
            break
    
            
    return result  
        

if __name__ == '__main__':
    #nums = [2,7,11,15]
    #target = 9
    
    nums = [3,2,4]
    target = 6
    
    result = twoSum(nums, target)
    print(result)
    