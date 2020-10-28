'''
Created on Oct 27, 2020

@author: sidteegela
'''


def spiralMatrix(matrix, m, n):
    
    result = []
    m = m  # No of rows
    n = n  # No of columns
    top = 0; bottom = m - 1; left = 0; right = n - 1
    direction = 0  # 0= right, 1= down, 2= left, 3= up
    
    while top <= bottom and left <= right:
        
        if direction == 0:  # Move right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1; direction += 1
        
        if direction == 1:  # Move down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1; direction += 1
                
        if direction == 2:  # Move left
            for i in reversed(range(left, right + 1)):
                result.append(matrix[bottom][i])
            bottom -= 1; direction += 1
                
        if direction == 3:  # Move up
            for i in reversed(range(top, bottom + 1)):
                result.append(matrix[i][left])
            left += 1; direction += 1
                
        direction = (direction + 1) % 4  # Resetting
            
    print(result)

# Time Complexity: O(n)
# Space: O(m*n)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    spiralMatrix(matrix, 3, 3)
    
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiralMatrix(matrix, 3, 4)
    
