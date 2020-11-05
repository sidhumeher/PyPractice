'''
Created on Nov 3, 2020

@author: sidteegela
'''
# Backtracking technique and DFS strategy


def exist(board, word):

    if len(board) == 0:
        return False
    
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, word):
                return True

    return False

    
def backtrack(row, col, suffix):
        
    rows = len(board)
    cols = len(board[0])
    
    # Exit condition
    if len(suffix) == 0:
        return True
    
    # Check boundaries before moving to backtracking
    if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != suffix[0]:
        return False
    
    ret = False
    
    # Marking the current cell
    board[row][col] = '*'
    
    # Explore all 4 directions- Up,Down,Right,Left
    for rowOffset, colOffset in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ret = backtrack(rowOffset, colOffset, suffix[1:])
        # Break first to do the cleanup before returning
        if ret:
            break  # Alternate: return True if found
    
    # Revert back marking    
    board[row][col] = suffix[0]
    
    # If not found, return False
    return ret
    

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = 'SEE'
    print(exist(board, word))
