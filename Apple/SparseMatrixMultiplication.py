'''
Created on Nov 11, 2020

@author: sidteegela
'''


def multiply(a, b):

    result = []
    
    # row_a = len(a) - 1
    row_b = len(b) - 1
    col_b = len(b[0]) - 1
    
    rowCount = 0;colCount = 0
    
    for row in a:
        newRow = []
        while rowCount <= row_b and colCount <= col_b:
            sum = 0
            for item in row:
                sum += item * b[rowCount][colCount]
                rowCount += 1
            newRow.append(sum)
            colCount += 1; rowCount = 0  # Reset rowCount
        colCount = 0  # Reset colCount
        result.append(newRow)

    return result

# Time Complexity:O(nk * ml),n rows and k items per row in A, m columns and l items per columns in B
# Space: O(No of rows of A * No of columns of B)


if __name__ == '__main__':
    a = [[ 1, 0, 0], [-1, 0, 3]]
    b = [[ 7, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 1 ]]
    print(multiply(a, b))
