'''
Created on Nov 19, 2020

@author: sidteegela
'''


# Brute force approach
def maxArea(height):
    
    # Max area = shortest vertical line * distance between lines
    
    maxarea = float('-inf')
    for i in range(len(height)):  # i = x-axis
        for j in range(i + 1, len(height)):  # j = y-axis
            maxarea = max(maxarea, (min(height[i], height[j]) * abs(i - j)))
            
    return maxarea

# Time complexity: O(n^2)- Time limit exceeds for larger inputs
# Space: O(1)

    
# Two pointer approach
def maxArea1(height):
    # start with 2 pointers on either side of input and move the pointer which is pointing to
    # shortest vertical line by one step
    maxarea = float('-inf')
    left = 0; right = len(height) - 1
    
    while left < right:
        maxarea = max(maxarea, (min(height[left], height[right]) * (right - left)))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return maxarea
    

if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea1(height))
    
    height = [1, 1]
    # print(maxArea(height))
    
    height = [4, 3, 2, 1, 4]
    # print(maxArea(height))
    
    height = [1, 2, 1]
    # print(maxArea(height))
