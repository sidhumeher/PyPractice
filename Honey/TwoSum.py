
# Two sum problem


# Brute force
def twoSum(nums, target):
    
    result = []
    
    for i in range(0, len(nums)):
        remain = target - nums[i]
        
        for j in range(i + 1, len(nums)):
            if nums[j] == remain:
                result.append([nums[i], nums[j]])
                
    return result
    
# Track items using dictionary


def twoSum1(nums, target):
    
    track = {}
    
    for index, item in enumerate(nums):
        remain = target - item
        if remain not in track:
            track[item] = index
        else:
            print(track)
            return [track[remain], index]
        
# Time: O(n)
# Space O(n) worst case
    
    
if __name__ == '__main__':
    nums = [2, 7, 11, 15]; target = 9
    print(twoSum(nums, target))
    
    nums = [3, 2, 4]; target = 6
    print(twoSum(nums, target))
    
    nums = [3, 3]; target = 6
    print(twoSum(nums, target))

    nums = [2, 7, 11, 15]; target = 9
    print(twoSum1(nums, target))
