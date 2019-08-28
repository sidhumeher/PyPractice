'''
Created on Aug 21, 2019

@author: siddardha.teegela
'''
import heapq

if __name__ == '__main__':
    ip = [2,1,3,5,4]
    
    #Convert a list to Heap data structure
    heapq.heapify(ip)
    print(list(ip))
    
    #Push element into Heap
    heapq.heappush(ip, 7)
    print('After Push:',list(ip))
    
    #Pop element from Heap
    heapq.heappop(ip)
    print('After Pop:',list(ip))
    
    li1 = [5, 7, 9, 4, 3]
    heapq.heapify(li1)
    
    #Push and Pop simultaneously
    #Element is pushed first and then pop operation happens
    print(heapq.heappushpop(li1, 2))
    
    li2 = [5, 7, 9, 4, 3]
    heapq.heapify(li2)
    
    #Element is popped first and then push happens
    print(heapq.heapreplace(li2, 2))
    print(list(li2))
    
    li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
    heapq.heapify(li1)
    
    #Display 3 largest elements
    print('3 largest elements:',heapq.nlargest(3, li1))
    
    #Display 3 smallest elements
    print('3 Smallest elements:', heapq.nsmallest(3, li1))