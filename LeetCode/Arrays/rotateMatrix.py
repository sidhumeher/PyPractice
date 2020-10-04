'''
Created on May 2, 2020

@author: sidteegela
'''

def rotate(matrix):
    
    #Using zip()
    #matrix[:] = zip(*matrix[::-1])
    
    #Using list comprehension
    matrix[:] = [[matrix[i] in matrix[::-1]] for i in range(len(matrix))]
    
    

if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    #rotate(matrix)
    #print(matrix)
    
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
  ]
    print(matrix)
    #print(matrix)