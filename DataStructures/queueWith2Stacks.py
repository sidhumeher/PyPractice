'''
Created on Jul 14, 2019

@author: siddardha.teegela
'''

from DataStructures.Stack import Stack

class queueWith2Stacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self,value):
        self.stack1.push(value)
        
    def dequeue(self):
        if not self.stack2.size() > 0:
            self.move_content()
        return self.stack1.pop()
    
    def move_content(self):
        while self.stack1.size() > 0:
            self.stack2.push(self.stack1.pop())