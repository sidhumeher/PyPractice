'''
Created on Nov 2, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def maxDepth_BST(node):

    if node == None:
        return 0
    
    return 1 + max(maxDepth_BST(node.left), maxDepth_BST(node.right))


if __name__ == '__main__':
    
    root = Node(3)
    node1 = Node(9)
    node2 = Node(20)
    
    root.left = node1
    root.right = node2
    
    node3 = Node(15)
    node4 = Node(7)
    
    node2.left = node3
    node2.right = node4
    
    print(maxDepth_BST(root))
    
