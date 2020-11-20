'''
Created on Nov 19, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = next
        
        
def reverseList(node):  # Pass head as input node
    
    if node == None:
        return Node
    
    prev = None; current = node; next = None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    return prev


if __name__ == '__main__':
    pass
