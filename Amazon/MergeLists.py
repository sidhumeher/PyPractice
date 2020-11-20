'''
Created on Nov 19, 2020

@author: sidteegela
'''


class Node(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(node):
    if node == None:
        return None
    result = []
    
    current = node
    while current:
        result.append(current.val)
        current = current.next
        
    return result        

        
def mergeLists(l1, l2):
    
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    
    head = temp = Node(0)
    
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 or l2
    
    return head.next    


if __name__ == '__main__':
    
    # 1->2->4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    
    node1.next = node2
    node2.next = node3
    
    # 1->3->4
    node4 = Node(1)
    node5 = Node(3)
    node6 = Node(4)
    
    node4.next = node5
    node5.next = node6
    
    result = mergeLists(node1, node4)
    print(printList(result))
        
