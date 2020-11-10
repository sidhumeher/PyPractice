'''
Created on Sep 3, 2019

@author: siddardha.teegela
'''
#Find the target element in the array. Return -1 if not present
#Run time complexity O(logn)

def search(nums, target):
        low = 0
        high = len(nums) - 1
        
        if not nums:
            return -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target == nums[mid] :
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
                    
        return -1

if __name__ == '__main__':
    ip = [4,5,6,7,0,1,2]
    target = 0
    
    result = search(ip, target)
    print('Target is at:',result)
    