'''
Created on Nov 8, 2020

@author: sidteegela
'''


def twoSum(nums, target):

    if len(nums) == 0:
        return

    track = {}  # save the current element and its index
    
    for index, value in enumerate(nums):
        remain = target - value
        if remain not in track:
            track[value] = index
        else:
            return [track[remain], index]
        

if __name__ == '__main__':
    nums = [2, 7, 11, 15]; target = 9
    print(twoSum(nums, target))
    
    nums = [3, 2, 4];target = 6
    print(twoSum(nums, target))
    
    nums = [3, 3]; target = 6
    print(twoSum(nums, target))
    
    nums = [-1, -2, -3, -4, -5]; target = -8
    print(twoSum(nums, target))
    
    nums = [-3, 4, 3, 90]; target = 0
    print(twoSum(nums, target))
