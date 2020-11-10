'''
Created on Jul 31, 2019

@author: siddardha.teegela
'''
class Node:
    def __init__(self, data, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def add_to_front(self, newData):
        new_node = Node(next = None, prev = None, data = newData)
        
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            
        # Move the head to point to new Node
        self.head = new_node
        
    def add_after(self, prevNode, newData):
        if prevNode is None:
            print('Node does not exist')
            return
        
        newNode = Node(data = newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if newNode.next is not None:
            newNode.next.prev = newNode
            
    def add_end(self, newData):
        newNode = Node(data = newData)
        newNode.next = None
        
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            return
        
        last = self.head
        while last is not None:
            last = last.next
        
        newNode.prev = last
        last.next = newNode
        
    def add_before(self, nextNode, newData):
        
        if nextNode is None:
            print('Node does not exist')
            return
        
        newNode = Node(data = newData)
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        newNode.next = nextNode
        
        if newNode.prev is not None:
            newNode.prev.next = newNode
        else:
            self.head = newNode
    
    def print(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next
    
if __name__ == '__main__':
    
    dll = DoublyLinkedList()
    
    dll.add_to_front(1)
    prevNode = Node(2)
    dll.add_after(dll.head,2)
    print(dll.print(dll.head))
    
    nextNode = Node(2)
    dll.add_before(nextNode, 3)
    print(dll.print(dll.head))
    