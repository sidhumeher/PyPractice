'''
Created on Jul 10, 2019

@author: siddardha.teegela
'''

class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self,value):
        return self.queue.insert(0,value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    
    def print(self):
        if self.size() == 0:
            print('Queue is empty')    
        else:
            for item in self.queue:
                print(item)
        
if __name__ == '__main__':
    q = Queue()
    
    #print('Size:', q.size())
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print()
    
    q.dequeue()
    q.dequeue()
    
    print('After dequeue')
    q.print()
    