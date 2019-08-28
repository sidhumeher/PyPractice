'''
Created on Jul 16, 2019

@author: siddardha.teegela
'''

from collections import deque

if __name__ == '__main__':
    dq = deque()
    
    #Append elements
    dq.append('Tom')
    dq.append('Hanks')
    
    print(dq)
    
    #Append Left
    dq.appendleft('Ab')
    print(dq)
    
    #Count
    print(dq.count('Tom'))
    
    #Extend right side
    dq.extend('Bb')
    print(dq)
    
    #Extend left side
    dq.extendleft('Aa')
    print(dq)
    
    #remove and return an element
    result = dq.pop()
    print(result)
    
    result= dq.popleft()
    print(result)
    
    #Reverses the elements and returns None
    print(dq.reverse())
    
    #Rotate Dequeue n steps to the right, -ve to rotate left
    dq.rotate(1)
    print(dq)
    