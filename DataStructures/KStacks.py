'''
Created on Jul 22, 2019

@author: siddardha.teegela
'''

class KStacks:
    def __init__(self, k, n):
        self.k = k #No of stacks
        self.n = n #Total size of array
        
        self.arr = [0]*self.n #Array which holds k stacks
        
        self.top = [-1]*self.k #All stacks are empty to begin with. -1 denotes stack is empty
        
        self.free = 0 #Top of free stack
        
        self.next = [i+1 for i in range(self.n)]
        self.next[self.n-1] = -1
        
    def isEmpty(self, sn):
        return self.top[sn] == -1
    
    def isFull(self):
        return self.free == -1
        
    def push(self, item, sn):
        if self.isFull():
            print('Stack overflow')
            return
        
        insert_at = self.free
        
        self.free = self.next[self.free]
        
        self.arr[insert_at] = item
        
        self.next[insert_at] = self.top[sn]
        
        self.top[sn] = insert_at
    

if __name__ == '__main__':
    #pass
    arr = [0]
    print(len(arr))
    print(arr)
    
    arr = [0]*5
    print(len(arr))
    print(arr)
    