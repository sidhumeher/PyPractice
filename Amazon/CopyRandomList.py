'''
Created on Nov 18, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

        
def copyList(node):

    if node == None:
        return None
    
    tracker = {}
    
    # helper method to track clone nodes or create if not created already 
    def getClone(node):
        if node == None:
            return None
        
        if node in tracker:
            return tracker[node]
        else:
            tracker[node] = Node(node.value, None, None)
            return tracker[node]
            
    head = current = node
    newNode = Node(head.value, None, None)
    tracker[head] = newNode
    
    while current:
        newNode.next = getClone(current.next)
        newNode.random = getClone(current.random)
        
        current = current.next
        newNode = newNode.next

    return tracker[head]

# Time complexity:O(n)
# Space complexity: O(n)


if __name__ == '__main__':
    pass
