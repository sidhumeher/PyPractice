'''
Created on Jul 10, 2019

@author: siddardha.teegela
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
            
    def push(self,value):
        return self.stack.append(value)
    
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

'''
if __name__ == '__main__':
    
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print(stack.stack)
    print(stack.pop())
    print(stack.peak())
'''