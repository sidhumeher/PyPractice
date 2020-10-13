'''
Created on Oct 10, 2020

@author: sidteegela
'''

# Making a deep copy of a linked list
# Approach: Iterating linked list


class Node:
    
    def __init__(self, x , next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class deepCopy():
    
    def __init__(self):
        self.visitedDict = {}  # Old node reference as key and clone node reference as value
    
    def getClonedNode(self, node):
        
        if node:  # If node exists
            if node in self.visitedDict:
                return self.visitedDict[node]  # If exists, return reference
            else:
                self.visitedDict[node] = Node(node.val, None, None)
                return self.visitedDict[node]  # If not exists, create and return references
            
        return None
    
    def copyRandomList(self, head):

        if head == None:
            return None
        
        oldHead = head
        newNode = Node(head.val, None, None)
        self.visitedDict[oldHead] = newNode
        
        while oldHead != None:
            newNode.random = self.getClonedNode(oldHead.random)
            newNode.next = self.getClonedNode(oldHead.next)
            
            oldHead = oldHead.next
            newNode = newNode.next
            
        return self.visitedDict[oldHead]

# Time Complexity: O(n)
# Space: O(n)


if __name__ == '__main__':
    pass
