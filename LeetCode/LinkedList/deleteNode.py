'''
Created on May 13, 2020

@author: sidteegela
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(head):
    
    current = ListNode(head.val)
    
    while current:
        print(current.val)
        current = current.next
            
def deleteNode(node):
        
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    #Head Node
    head = ListNode(4)
    firstNode = ListNode(5)
    secondNode = ListNode(1)
    thirdNode = ListNode(9)
    
    head.next = firstNode
    firstNode.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = None
    
    printLinkedList(head)
    deleteNode(firstNode)

