'''
Created on Nov 19, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addList(l1, l2):
    
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    
    carry = 0
    head = temp = Node()
    
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
            
        temp.next = Node(carry % 10)
        temp = temp.next
        carry //= 10
        
    return head.next


def printList(node):
    if node == None:
        return None
    result = []
    
    current = node
    while current:
        result.append(current.val)
        current = current.next
        
    return result


if __name__ == '__main__':
    # 2->4->3
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(3)
    
    node1.next = node2
    node2.next = node3
    
    # 5->6->4
    node4 = Node(5)
    node5 = Node(6)
    node6 = Node(4)
    
    node4.next = node5
    node5.next = node6
    
    result = addList(node1, node4)
    print(printList(result))
