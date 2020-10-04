'''
Created on Apr 18, 2020

@author: sidteegela
'''

def intersect(nums1, nums2):
    
    result = []
    nums1.sort()
    nums2.sort()
    
    #print(nums1)
    #print(nums2)
    x = 0 
    y = 0
    
    while x < len(nums1):
        if nums1[x] in nums2[y:]:
            result.append(nums1[x])
            y = nums2.index(nums1[x]) + 1
            #y = x + 1
        x += 1
    
    '''
    while x < len(nums1):
        if nums1[x] in nums2:
            result.append(nums1[x])
        x += 1
    '''   
    return result 

if __name__ == '__main__':
    num1 = [1,2,2,1]
    num2 = [2,2]
    
    #result = intersect(num1, num2)
    #print(result)
    
    num1 = [4,9,5]
    num2 = [9,4,9,8,4]
    
    #result = intersect(num1, num2)
    #print(result)
    
    num1 = [2,1]
    num2 = [1,2]
    
    #result = intersect(num1, num2)
    #print(result)
    
    num1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,
            58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,
            62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,
            65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,
            66,82,0,79,11,81]

    num2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,
            85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
    
    #result = intersect(num1, num2)
    #print(result)
    
    
    num1 = [1,2,2,1]
    num2 = [2,2]
    result = intersect(num1, num2)
    print(result)
    