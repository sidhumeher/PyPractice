'''
Created on Feb 18, 2019

@author: siddardha.teegela
'''

if __name__ == '__main__':
    testList = [1,2,3,4,5,67,8,9]
    
    for item in testList:
        if item == 9:
            print(item)
            break
    else:
        print('Item not found')
        
        
    for item in testList:
        if item == 10:
            print(item)
            break
    else:
        print('Item not found')
    