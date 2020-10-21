'''
Created on Oct 20, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def maxHeight(node):
    
    if node == None:
        return 0
    
    leftmaxheight = maxHeight(node.left)
    rightmaxheight = maxHeight(node.right)
    
    maxheight = max(leftmaxheight, rightmaxheight) + 1

    return maxheight


if __name__ == '__main__':
    
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    root.left = node2
    root.right = node3
    
    node4 = Node(4)
    node5 = Node(5)
    
    node2.left = node4
    node2.right = node5
    
    height = maxHeight(root)
    print('Max Height: ', height)
    
    root1 = Node(1)
    print('Max Height: ', maxHeight(root1))
