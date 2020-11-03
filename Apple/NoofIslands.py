'''
Created on Nov 2, 2020

@author: sidteegela
'''


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
        
    grid[i][j] == '#'
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
        
        
def numIslands(grid):
        
    result_count = 0
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                result_count += 1
                    
    return result_count

# Time complexity: o(n*m), n=No of rows, m=No of columns


if __name__ == '__main__':
    grid = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
  ]
    
    print(numIslands(grid))
