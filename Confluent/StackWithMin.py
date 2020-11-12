'''
Created on Nov 12, 2020

@author: sidteegela
'''
# Stack with a getMinimum() method that returns current minimum value in stack
# This stack is implemented with custom Node data structure and a dequeue to track minimum value

'''
Time complexity for all stack operations are done in O(1) time
Also for the dequeue, the push and pop are done in O(1) time

Space complexity: Stack takes O(n) space based on n items pushed
And for dequeue the worst space complexity can be O(n) in the case where
values of all items pushed to stack are in decreasing order of their value
'''

from collections import deque


class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return "Node:{}".format(self.data)
    
    
class Stack(object):
    
    def __init__(self):
        self.top = None  # Top of the stack
        self.min = None  # Minimum value of stack
        self.dq = deque()  # To track the minimum item in stack
    
    def __str__(self):
        temp = self.top
        result = []
        
        while temp:
            result.append(temp.data)
            temp = temp.next
            
        return ('Stack: {}'.format(result))
        
    def getMinimum(self):
        if self.top == None:
            print('Stack is empty')
            return
        else:
            return self.min  # Returns current Minimum value of stack
        
    def peek(self):
        if self.top == None:
            print('Stack is empty')
            return
        else:
            print(self.top.value)
            
    def push(self, value):
        newNode = Node(value)
        if self.top == None:
            self.top = newNode
            self.min = self.top.data
            self.dq.append(self.top.data)  # Update the current minimum value
        else:
            newNode.next = self.top
            self.top = newNode  # updating top of stack
            # Check for minimum value in dequeue
            if newNode.data < self.dq[0]:
                self.dq.appendleft(newNode.data)
                self.min = self.dq[0]
            
    def pop(self):
        
        if self.top == None:
            print('Stack is empty')
            return 
        else:
            poppedNode = self.top
            self.top = self.top.next
            poppedNode.next = None
            # check dequeue if popped item is the minimum value
            if poppedNode.data == self.dq[0]:
                self.dq.popleft()
                self.min = self.dq[0]  # updated stack minimum value
            return poppedNode.data


if __name__ == '__main__':
    newstack = Stack()
    
    # Push items
    newstack.push(5)
    newstack.push(2)
    newstack.push(3)
    newstack.push(1)
    newstack.push(9)
    
    # print stack
    print(newstack)
    print('Min:', newstack.getMinimum())
    
    # pop item
    print('PoppedItem:', newstack.pop())
    print(newstack)
    print('Min:', newstack.getMinimum())
    print('PoppedItem:', newstack.pop())
    print(newstack)
    print('Min:', newstack.getMinimum())
    
    # push
    newstack.push(9)
    newstack.push(1)
    newstack.push(0)
    
    print(newstack)
    
    # pop items
    print('Min:', newstack.getMinimum())
    print('PoppedItem:', newstack.pop())
    print(newstack)
    print('Min:', newstack.getMinimum())
    print('PoppedItem:', newstack.pop())
    print(newstack)
    print('Min:', newstack.getMinimum())
    
