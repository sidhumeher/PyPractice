'''
Created on Nov 22, 2020

@author: sidteegela
'''


def mergeSort(nums):
    
    # split input into two halfs
    if len(nums) > 1:
        mid = len(nums) // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        # Recursion
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
           
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            
            nums[k] = left[i]
            i += 1; k += 1
            
        while j < len(right):
            
            nums[k] = right[j]
            j += 1; k += 1
            
    print(nums)


if __name__ == '__main__':
    nums = [7, 5, 3]
    mergeSort(nums)
