'''
Created on Dec 1, 2020

@author: sidteegela
'''


def floodFill(image, sr, sc, newColor):
    
    currentColor = image[sr][sc]
    lrow = len(image)
    lcol = len(image[0])
    
    if currentColor == newColor:
        return image
    
    def dfs(image, row, col):
        if row < 0 or col < 0 or row >= lrow or col >= lcol or image[row][col] != currentColor:
            return
        
        image[row][col] = newColor
        
        dfs(image, row - 1, col)
        dfs(image, row + 1, col)
        dfs(image, row, col - 1)
        dfs(image, row, col + 1)
    
    dfs(image, sr, sc)
    return image

# Time complexity: O(n)
# Space: O(n), call stack


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1; sc = 1; newColor = 2
    
    print(floodFill(image, sr, sc, newColor))
