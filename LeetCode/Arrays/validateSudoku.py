'''
Created on Apr 25, 2020

@author: sidteegela
'''

def isValidSudoku(board):
    
    
    #Leet code simpler way of checking matrices. Time 100 MS
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = []
            for m in range(i,i+3):
                for n in range(j,j+3):
                    if board[m][n] != ".":
                        box.append(board[m][n])
                if len(set(box)) != len(box):
                    return False 
    
    # My solution below. Time 156 MS
    '''
    #Matrices checking
    matrixValidator = []
    index = 0
    start_board = 0
    end_board = 3
    start_row = 0
    end_row = 3
    
    #print('First row of 3 matrices')
    while index < 3:
        matrixValidator.clear()
        for curr_list in board[start_board:end_board]:
            #print(curr_list[start_row:end_row])
            for item in curr_list[start_row:end_row]:
                if item.isdigit():
                    matrixValidator.append(item)
        #print(matrixValidator)
        if len(matrixValidator) != len(set(matrixValidator)):
            return False
        index += 1  
        start_row += 3
        end_row += 3
    
    #Resetting values
    matrixValidator.clear()
    index = 0
    start_board = 3
    end_board = 6
    start_row = 0
    end_row = 3
    #print('Second row of 3 matrices')
    while index < 3:
        matrixValidator.clear()
        for curr_list in board[start_board:end_board]:
            #print(curr_list[start_row:end_row])
            for item in curr_list[start_row:end_row]:
                if item.isdigit():
                    matrixValidator.append(item)
                    
        #print(matrixValidator)
        if len(matrixValidator) != len(set(matrixValidator)):
            return False
        index += 1  
        start_row += 3
        end_row += 3
     
    #Resetting values
    matrixValidator.clear()
    index = 0
    start_board = 6
    end_board = 9
    start_row = 0
    end_row = 3
    #print('Third row of 3 matrices')
    while index < 3:
        matrixValidator.clear()
        for curr_list in board[start_board:end_board]:
            #print(curr_list[start_row:end_row])
            for item in curr_list[start_row:end_row]:
                if item.isdigit():
                    matrixValidator.append(item)
        
        #print(matrixValidator)
        if len(matrixValidator) != len(set(matrixValidator)):
            return False
        index += 1  
        start_row += 3
        end_row += 3
    '''
     
    #Row checking
    rowValidator = []
    for currList in board:
        rowValidator.clear()
        for item in currList:
            if item.isdigit():
                rowValidator.append(item)
        #print(rowValidator)
        if len(rowValidator) != len(set(rowValidator)):
            return False
        
    #Column checking
    columnValidator = []
    columnIndex = 0
    item = 0
    
    while columnIndex < 9:
        columnValidator.clear()
        for currList in board:
            if currList[item].isdigit():
                columnValidator.append(currList[item])
        
        if len(columnValidator) != len(set(columnValidator)):
            return False
        item += 1
        columnIndex += 1    
    
    return True

if __name__ == '__main__':
    
    
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
  ]
  
    '''
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
  ]
  '''
    
    result = isValidSudoku(board)
    if result == True:
        print('Valid Sudoku')
    else:
        print('Invalid Sudoku')