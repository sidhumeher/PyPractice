'''
Created on May 7, 2019

@author: siddardha.teegela
'''
from pip._vendor.html5lib.treewalkers import pprint
def queensAttack(n, k, r_q, c_q, obstacles):
    row = r_q
    col = c_q
    possibilities = 0
    possArr = []
        
    ''' Moving diagonal Q4'''
    q4 = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row > 1 and col < n:
            row -= 1
            col += 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            q4.append([row,col])
        else:
            break
        
    row = r_q
    col = c_q
    ''' Moving diagonal Q3'''
    q3 = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row != 1 and col != 1:
            row -= 1
            col -= 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            q3.append([row,col])
        else:
            break
    
    row = r_q
    col = c_q
    ''' Moving diagonal Q2'''
    q2 = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row < n and col > 1:
            row += 1
            col -= 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            q2.append([row,col])
        else:
            break
    
    row = r_q
    col = c_q
    ''' Moving diagonal Q1'''
    q1 = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row < n and col < n:
            row += 1
            col += 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            q1.append([row,col])
        else:
            break
        
    ''' Resetting row,col'''
    row = r_q
    col = c_q
    ''' Moving left'''
    left = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if col <= n and col > 1:
            col -= 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            left.append([row,col])
        else:
            break
    
    row = r_q
    col = c_q
    ''' Moving right'''
    right = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if col == n:
            break
        elif col >= 1:
            col += 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            right.append([row,col])
        else:
            break
    
    row = r_q
    col = c_q
    ''' Moving north'''
    north = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row == n:
            break
        elif row < n:
            row += 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            north.append([row,col])
        else:
            break
    
    row = r_q
    col = c_q
    ''' Moving south'''
    south = []
    while row >= 1 and row <= n and col >= 1 and col <= n :
        if row == 1:
            break
        elif row >1:
            row -= 1
            #print(row,col)
            possibilities += 1
            possArr.append([row,col])
            south.append([row,col])
        else:
            break
        
    ''' Check for obstacles'''
    '''for obstacle in obstacles:
        if obstacle in possArr:
            possibilities -= 1
    '''
       
    ''' Check for obstacles'''
    for obstacle in obstacles:
        row = obstacle[0]
        col = obstacle[1]
        if obstacle in right:
            #print(right)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if col == n:
                    break
                elif col >= 1:
                    col += 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in left:
            #print(left)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if col <= n and col > 1:
                    col -= 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in north:
            #print(north)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row == n:
                    break
                elif row < n:
                    row += 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in south:
            #print(south)
            possibilities -= 1 # Removing the obstacle itself as possibility
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row == 1:
                    break
                elif row >1:
                    row -= 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in q4:
            #print(q4)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row > 1 and col < n:
                    row -= 1
                    col += 1
                    possibilities -= 1            
                else:
                    break
        elif obstacle in q3:
            #print(q3)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row != 1 and col != 1:
                    row -= 1
                    col -= 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in q2:
            #print(q2)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row < n and col > 1:
                    row += 1
                    col -= 1
                    possibilities -= 1
                else:
                    break
        elif obstacle in q1:
            #print(q1)
            possibilities -= 1
            while row >= 1 and row <= n and col >= 1 and col <= n :
                if row < n and col < n:
                    row += 1
                    col += 1
                    possibilities -= 1
                else:
                    break
       
    return possibilities
    

if __name__ == '__main__':
    
    ''' No of rows/columns'''
    n = 4
    ''' No of obstacles'''
    k = 0
    ''' Row position of queen'''
    r_q = 4
    ''' Column position of queen'''
    c_q = 4
    ''' obstacles array'''
    obstacles = []
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    result = queensAttack(5, k, 4, 3, [[5, 5], [4, 2], [2, 3]])
    result = queensAttack(5, k, 4, 4, [[5, 5], [4, 2], [2, 3]])
    print(result)
    #queensAttack(5, k, 4, 1, obstacles)