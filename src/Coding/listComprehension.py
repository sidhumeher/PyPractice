'''
Created on Dec 27, 2018

@author: siddardha.teegela
'''

if __name__ == '__main__':
    newList = []
    oldList = [1,2,3,4,5]
    
    '''
    List Comprehension
    [expression for item in list if condition]
    '''
     
    newList = [item*2 for item in oldList if item > 1]
    print (newList)