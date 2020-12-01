'''
Created on Nov 30, 2020

@author: sidteegela
'''


# Overwriting the given input grid
def numofislands(grid):
    
    count = 0

    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        dfs(grid, i - 1, j)
        dfs(grid, i + 1, j)
        dfs(grid, i, j - 1)
        dfs(grid, i, j + 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
                
    return count


# Without changing the input grid
def numofislands1(grid):
    
    count = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    def dfs(grid, i, j, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'\
        or visited[i][j] == True:
            return

        visited[i][j] = True
        dfs(grid, i - 1, j, visited)
        dfs(grid, i + 1, j, visited)
        dfs(grid, i, j - 1, visited)
        dfs(grid, i, j + 1, visited)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and visited[i][j] != True:
                count += 1
                dfs(grid, i, j, visited)

    return count


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]]
    print(numofislands(grid))
    
    grid = [["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]]
    print(numofislands1(grid))
