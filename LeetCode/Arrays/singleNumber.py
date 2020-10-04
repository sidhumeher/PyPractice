'''
Created on Apr 13, 2020

@author: sidteegela
'''
from collections import Counter

def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    
    counter = Counter(nums)
    print(counter)
    
    for key in counter:
        if counter[key] == 1:
            print(key)
            return key


if __name__ == '__main__':
    nums = [2,2,1]
    result = singleNumber(nums)
    print(result)
    
    nums = [4,1,2,1,2]
    result = singleNumber(nums)
    print(result)