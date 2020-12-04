'''
Created on Dec 3, 2020

@author: sidteegela
'''


# Print ANIMAL if num is divisible by 32
def printAnimal(num):
    
    if num == 0:
        print('Invalid input')
        return
    if num % 32 == 0:
        print('ANIMAL')
    elif num % 16 == 0:
        print('ANIM')
    elif num % 8 == 0:
        print('AN')


# Find second largest num in list
def secondLargest(nums):

    if len(nums) == 0:
        return 0

    firstLarge = float('-inf')
    secondLarge = float('-inf')
    
    for item in nums:
        if item > firstLarge:
            secondLarge = firstLarge
            firstLarge = item
            
    return secondLarge


# Largest sum of consecutive integers in an array
def largestSum(nums):

    if len(nums) == 0:
        return 0
    
    largestSum = float('-inf')
    currentSum = 0

    for item in nums:
        currentSum += item
        if currentSum > largestSum:
            largestSum = currentSum
        if currentSum < 0:
            currentSum = 0
            
    return largestSum

# Time complexity: O(n)


# String compress
def strCompress(s):

    if len(s) == 0:
        return None

    result = []
    count = 1
    pointer = s[0]
    
    for index in range(1, len(s)):
        if s[index] == pointer:
            count += 1
        else:
            result.append(pointer + str(count))
            count = 1  # reset
        pointer = s[index]
        
    result.append(pointer + str(count))
    return ''.join(result)

# Time complexity: O(n)
# Space: O(n), n = length of input-worst case


# Remove duplicates from list and print
def removeDuplicates(nums):
    
    if len(nums) == 0:
        return None
    
    '''
    # Using set
    s = set()
    
    for item in nums:
        if item in s:
            print(item)
        else:
            s.add(item)

    return list(s)
    '''
    '''
    # Using dictionary
    track = {}
    
    for item in nums:
        if item not in track:
            track[item] = 1
        else:
            print(item)
            
    return list(track.keys())
    '''

    # Using list
    result = []
    for item in nums:
        if item not in result:
            result.append(item)
        else:
            print(item)
            
    return result


if __name__ == '__main__':
    nums = [3, 1, 4, 5, 3, 6, 2, 9]
    print(secondLargest(nums))
    
    nums = [-2, 3, 2, -1]
    print(largestSum(nums))
    
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(largestSum(nums))

    s = 'aabbbccccaaa'
    print(strCompress(s))
    
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(removeDuplicates(nums))
    
