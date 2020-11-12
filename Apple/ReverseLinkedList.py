'''
Created on Nov 11, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
def reverseLinkedList(node):
    
    if node is None:
        return 
    
    prev = None; curr = node; next = None
    
    while curr:
        next = curr
        curr.next = prev
        prev = curr
        curr = next
        
    return prev


if __name__ == '__main__':
    pass
