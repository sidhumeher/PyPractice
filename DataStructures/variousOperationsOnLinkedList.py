'''
Created on Jun 27, 2019

@author: siddardha.teegela
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def display_elements(Node):
    current = Node
    
    while current is not None:
        print(current.data)
        current = current.next

def remove_duplicates(Node):
    elements = dict()
    
    current = Node
    prev = Node
    while current is not None:
        if current.data not in elements:
            elements.update({current.data:1})
        else:
            if current.next is None:
                prev.next = None
            else:
                prev.next = current.next.next
        prev = current
        current = current.next
    
    display_elements(Node)
    
def Kth_to_last(Node,k):
    currentCount = 1
    
    current = Node
    while current is not None:
        if currentCount != k:
            currentCount += 1
        else:
            print(current.data)
        current = current.next


def delete_node(Node,position):
    
    if Node is None or Node.next == None:
        return Node
    
    currentNode = 1
    current = Node
    prev = Node
    
    while current is not None:
        if currentNode != position:
            currentNode += 1
        else:
            if current is None or current.next == None:
                prev.next = None
                break
            else:
                prev.next = current.next.next
        prev = current
        current = current.next
    
    display_elements(Node)

def add_linkedlists(Node1,Node2,direction):
    
    current1 = Node1
    linkedList1_num = ''
    
    current2 = Node2
    linkedList2_num = ''
    
    while current1 is not None:
        linkedList1_num += str(current1.data)
        current1 = current1.next
        
    while current2 is not None:
        linkedList2_num += str(current2.data)
        current2 = current2.next
    
    if direction == 'Left':
        linkedList1_num = linkedList1_num[::-1]
        linkedList2_num = linkedList2_num[::-1]
        print(int(linkedList1_num) + int(linkedList2_num))
    else:
        print(int(linkedList1_num) + int(linkedList2_num))
    
    

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    
    ''' 
    Before removing duplicates
    '''
    print('###DISPLAY ELEMENTS###')  
    display_elements(node1)
    
    '''
    Remove duplicates
    '''
    print('###REMOVE DUPLCIATES###')
    #remove_duplicates(node1)
    
    '''
    Get Kth to last element from linked list
    '''
    print('###Kth to last element###')
    Kth_to_last(node1,3)
    
    '''
    Delete a node from Linked list
    '''
    print('###Delete element###')
    #delete_node(node1,5)
    
    '''
    Adding 2 Linked Lists from Left or Right
    '''
    print('### Adding elements of 2 Linked lists from Left or Right###')
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.next = node2
    node2.next = node3
    node3.next = None
    
    node4 = Node(8)
    node5 = Node(7)
    
    node4.next = node5
    node5.next = None
    
    add_linkedlists(node1,node4,'Left')
    add_linkedlists(node1,node4,'Right')
    
    