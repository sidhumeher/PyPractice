'''
Created on Nov 8, 2020

@author: sidteegela
'''


# Brute force: O(n^3)
def threeSum_bf(nums, target):
    
    if len(nums) == 0:
        return []
    result = []

    for i in range(0, len(nums)):
        remain = target - nums[i]
        for j in range(i + 1, len(nums)):
            remain2 = remain - nums[j]
            for k in range(j + 1, len(nums)):
                if nums[k] == remain2:
                    result.append([nums[i], nums[j], nums[k]])
    return result

# Two pointer approach
'''
Sort the list first. Any duplicates will be adjacent then. For every current element
check its previous element to avoid duplicates and then use two sum problem
'''


def threeSum_2pointer(nums, target):
    
    result = []
    nums.sort()  # Sort first
    
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:  # Avoiding duplicates
            twoSum(nums, i , result)
        
    return result


# Three sum broken into two sum problem    
def twoSum(nums, i , result):
    low = i + 1
    high = len(nums) - 1
    
    while low < high:
        sum = nums[i] + nums[low] + nums[high]
        if sum < 0:
            low += 1
        elif sum > 0:
            high -= 1
        else:
            result.append([nums[i], nums[low], nums[high]])
            low += 1; high -= 1
            # Avoiding duplicate
            while low < high and nums[low] == nums[low - 1]:
                low += 1
# Time complexity: O(n^2). Two sum is O(n). Sorting takes O(n logn) time
# Total time equals to O(N^2)
# Space: O(logn) to O(n) based on sorting algorithm


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]; target = 0
    # print(threeSum_bf(nums, target))
    print(threeSum_2pointer(nums, target))
