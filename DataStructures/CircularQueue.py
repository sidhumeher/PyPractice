'''
Created on Aug 19, 2019

@author: siddardha.teegela
'''

class CircularQueue:
    
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
        
    def enqueue(self, data):
        if self.front == 0 and self.rear == self.size-1 or self.rear == self.front-1:
            print('Queue is full')
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            
    def dequeue(self):
        if self.front == self.rear == -1:
            print('Queue is empty')
            return
        elif self.front == self.rear:
            returnValue = self.queue[self.front]
            self.front,self.rear = -1
            return returnValue
        else:
            returnValue = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return returnValue
            
    def display(self):
        if self.front == -1:
            print('Queue is empty')
            return
        elif self.rear > self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end=' ')
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')

if __name__ == '__main__':
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.display()
    
    print('\nDeleting an element')
    cq.dequeue()
    cq.display()
    
    print()
    cq.enqueue(5)
    cq.display()