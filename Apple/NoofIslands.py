'''
Created on Nov 2, 2020

@author: sidteegela
'''


def dfs(grid, i, j):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
        return
    else:
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
                result_count += 1
                dfs(grid, i, j)
                                    
    return result_count

# Time complexity: o(n*m), n=No of rows, m=No of columns


def isSafe(i, j): 
        return (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and 
                not visited[i][j] and grid[i][j]) 


# DFS search on matrix
def dfs1(i, j):
    # Rows and columns of all neighboring items for a given cell
    rowNumber = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNumber = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    # mark current cell as visited
    visited[i][j] = True
    print('Inside dfs')
    
    # Recurse all neighbors
    for k in range(len(rowNumber)):
        if isSafe(i + rowNumber[k], j + colNumber[k]):
            dfs1(i + rowNumber[k], j + colNumber[k])
    
    
# Not modifying the input matrix    
def countOfIslands(grid):
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] == False and grid[i][j] == 1:
                dfs1(i, j)
                count += 1
    return count

# Time complexity: O(rows*columns)


if __name__ == '__main__':
    grid = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
  ]
    # print(numIslands(grid))
    
    # tracking matrix
    visited = [[False for j in range(len(grid[0]))]for i in range(len(grid))]
    print(countOfIslands(grid))
    
