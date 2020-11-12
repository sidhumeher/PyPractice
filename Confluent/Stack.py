'''
Created on Nov 11, 2020

@author: sidteegela
'''

# A special stack which supports getMin() in O(1) time complexity and O(1) extra space
'''
minEle will track current min element on stack
For push: If x< minELe, insert (2*x - minEle) and make x minEle
For pop: If y <minEle, the new (minEle = 2*minEle - y)
'''


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return "Node({})".format(self.value)
    
    __repr__ = __str__

    
class Stack:
    
    def __init__(self):
        self.top = None
        self.count = 0
        self.min = None
        
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(self.top)
            temp = temp.next
        return ('Stack: {}'.format(out))
    
    def getMin(self):
        if self.top is None:
            print('Stack is empty')
        else:
            return self.min
            
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def __len__(self):
        self.count = 0
        temp = self.top
        while temp:
            temp = temp.next
            self.count += 1
        return self.count
    
    def peek(self):
        if self.top is None:
            print('Stack is empty')
        else:
            if self.top.value < self.min:
                return self.min
            else:
                return self.top.value
            
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.min = value
            
        elif value < self.min:
            temp = (2 * value) - self.min
            newNode = Node(temp)
            newNode.next = self.top
            self.top = newNode
            self.min = value
        else:
            newNode = Node(value)
            newNode. next = self.top
            self.top = newNode
        print('Node inserted:', value)
        
    def pop(self):
        
        if self.top is None:
            print('Stack empty')
            return
        
        removeNode = self.top.value
        self.top = self.top.next
        if removeNode < self.min:
            print('Removed:', self.min)
            self.min = (2 * self.min) - removeNode
        else:
            print('Removed:', removeNode)


if __name__ == '__main__':
    
    s = Stack()
    
    s.push(3)
    s.push(5)
    print('Min:', s.getMin())
    s.push(1)
    print('Min:', s.getMin())
    s.pop()
    print('Min:', s.getMin())
    
    print(s)
