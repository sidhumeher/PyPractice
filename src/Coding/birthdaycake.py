'''
Created on Jan 10, 2019

@author: siddardha.teegela
'''


'''
Concept: using max() to find the largest number in list. And use count() to 
find the no of occurences of an element in list
'''

def birthdayCakeCandles(ar):
    maxInList = max(ar)
    return ar.count(maxInList)

if __name__ == '__main__':
    ar = [3,2,1,3]
    result = birthdayCakeCandles(ar)
    print(result)
