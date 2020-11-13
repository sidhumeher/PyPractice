'''
Created on Nov 12, 2020

@author: sidteegela
'''

# Find cycle in linked list


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        

# Time complexity: O(n)
# Space: O(1)        
def cycle(node):
    
    if node == None:
        return 
    
    slow = node; fast = node
    
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print('Cycle exists')
            return


if __name__ == '__main__':
    pass
