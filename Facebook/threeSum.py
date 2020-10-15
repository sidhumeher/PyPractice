'''
Created on Oct 11, 2020

@author: sidteegela
'''


def threeSum(nums):
    '''
    def helper(num1, num2):
        return num1 + num2
        
    if len(nums) == 0 or nums == [0]:
        return []
    
    result = []
    i, j = 0, 0
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums) - 2):
            if nums[i] + helper(nums[j], nums[j + 1]) == 0:
                result.append([nums[i], nums[j], nums[j + 1]])
    
    print(result)
    '''
    
    result = set()
    dups = set()
    seen = {}

    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i + 1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    result.add(tuple(sorted([val1, val2, complement])))
                seen[val2] = i
                print(seen[val2])
    
    return result

# Time complexity: O(n^2)
# Space: O(n) for set and directory

    
if __name__ == '__main__':
    
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum(nums)
    for item in result:
        print(item)
