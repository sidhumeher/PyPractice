
#Demo for list creation in python

import copy
import bisect

if __name__ == '__main__':
    arr1 = [3,5,7,9]
    arr2 = list(range(5))
    arr3 = [1] + [0]*5
    
    print(arr1)
    print(arr2)
    print(arr3)
    print('###Shallow and Deep copy demo####')
    #List copy in Python
    
    list1 = [1,2,3,4,5]
    
    #Shallow copy- Change to new list will change the original list
    list2 = list1.copy()
    list2[3] = 9
    print('Originallist:',list1)
    print('Newlist',list2)
    
    #Deep copy- Changes made to new list does not affect original list
    
    list1 = [10,11,12,13,14]
    list2 = copy.deepcopy(list1)
    
    list2[3] = 99
    
    print('Orignal list:',list1)
    print('New list:', list2)
    
    print('##############')
    
    #bisect module demo
    
    bisectList = [1,2,3,4,5,6]
    
    #Returns the rightmost index to insert
    print(bisect.bisect(bisectList, 7, 0, len(bisectList)))
    #Returns the leftmost index to insert
    print(bisect.bisect_left(bisectList, 3, 0, len(bisectList)))
    #Return the rightmost index to insert
    print(bisect.bisect_right(bisectList, 4, 0, len(bisectList)))
    print('##############')
    
    #Returns a sorted list after insertion
    bisect.insort(bisectList, 3, 0, len(bisectList))
    print(bisectList)
    
    bisect.insort_right(bisectList, 7)
    print(bisectList)
    