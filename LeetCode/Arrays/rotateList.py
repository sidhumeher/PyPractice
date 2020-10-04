'''
Created on Apr 13, 2020

@author: sidteegela
'''

def rotate(input):
    pass

if __name__ == '__main__':
    inputList = [1,2,3,4,5,6,7]
    
    #print(rotate(inputList))
    
    #print(inputList.pop())
    #print(inputList)
    
    poppedItem = inputList.pop()
    inputList.insert(0, poppedItem)
    print(inputList)