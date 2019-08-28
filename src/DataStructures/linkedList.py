'''
Created on Feb 2, 2019

@author: siddardha.teegela
'''

class Node(object):
    
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node = new_next
    
class LinkedList(object):
        
    def __init__(self,head=None):
        self.head = head
    
    def insert_atHead(self,data): #Pushing the head to next
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode
        
    def insert_between(self,middle_node,data):
        if middle_node is None:
            print('Middle node does not exist')
            return
        
        newNode = Node(data)
        newNode.next_node = middle_node.next_node
        middle_node.next_node = newNode
        
    
    def insert_atEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode is not None:
            lastNode = lastNode.next_node
        lastNode.next_node = newNode
        
    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            count +=1
        return count
    
    def search(self,data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
                
        if current is None:
            print('Data could not be found')
        else:
            return current
        
    def delete(self,data):
        current = self.head
        previous = None
        found = False
        
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if current is None:
            print("Data not found in Linkedlist")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
if __name__ == '__main__':
    pass