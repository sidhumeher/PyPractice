'''
Created on Jul 30, 2019

@author: siddardha.teegela
'''

from DataStructures import Queue

class StackwithOneQueue:
    
    def __init__(self):
        self.queue = Queue.Queue()
    
    def push(self,element):
        size = len(self.queue.queue)
        self.queue.enqueue(element)
        
        for i in range(size):
            popped = self.queue.dequeue()
            self.queue.enqueue(popped)
            
    def pop(self):
        return self.queue.dequeue()
        
    def isEmpty(self):
        return self.queue.is_empty()
    
    def top(self):
        return self.queue.queue[-1]

if __name__ == '__main__':
    
    s = StackwithOneQueue()
    
    s.push(1)
    s.push(2)
    s.push(3)
    
    print('Top:', s.top())
    
    s.pop()
    print('Top:', s.top())
    
    s.push(4)
    print('Top:', s.top())
     