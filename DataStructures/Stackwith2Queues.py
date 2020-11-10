'''
Created on Jul 17, 2019

@author: siddardha.teegela
'''

from DataStructures import Queue

class Stackwith2Queues:
    def __init__(self):
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()
        
        #Maintain current no of elements
        self.curr_size = 0
    
    def push(self,value):
        self.curr_size += 1
        self.queue1.enqueue(value)
        
        while(not self.queue1.is_empty()):
            self.queue2.enqueue(self.queue1.dequeue())
            
        self.q = self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.q
        
    def pop(self):
        self.curr_size -= 1
        return self.queue1.queue.pop(0)
        
    def top(self):
        if(self.queue1.is_empty()):
            return -1
        return self.queue1.queue[0]

    def size(self):
        return self.curr_size
    

if __name__ == '__main__':
    s = Stackwith2Queues()
    
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    
    print('Top:',s.top())
    print('Size',s.size())
    print(s.queue1.queue)
    
    print(s.pop())
    
    print('Top:',s.top())
    print('Size',s.size())
    print(s.queue1.queue)
    
    