'''
Created on Nov 2, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sameTree(root1, root2):
    
    '''
    if root1 == None and root2 == None:
        return True
    elif root1 == None and root2 != None:
        return False
    elif root1 != None and root2 == None:
        return False
    
    if root1.left != None and root2.left != None:
        if root1.left.data == root2.left.data:
            return sameTree(root1.left, root2.left)
        else:
            return False
            
    if root1.right != None and root2.right != None:
        if root1.right.data == root2.right.data:
            return sameTree(root1.right, root2.right)
        else:
            return False

    return False
    '''
    if root1 == None and root2 == None:
        return True
    elif root1 == None and root2 != None:
        return False
    elif root1 != None and root2 == None:
        return False
    elif root1.data != root2.data:
        return False

    return sameTree(root1.left, root2.left) and \
        sameTree(root1.right, root2.right)

# Time complexity O(n)
# Space: O(log n) for balanced tree and O(n) for unbalanced tree


def sameTree1(root1, root2):
    
    if root1 == None and root2 == None:
        return True

    elif root1 == None and root2 != None:
        return False
    elif root1 != None and root2 == None:
        return False
    elif root1.data != root2.data:
        return False
    else:
        return sameTree1(root1.left, root2.left) and sameTree1(root1.right, root2.right)

    
if __name__ == '__main__':
    
    root1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    root1.left = node2
    root1.right = node3
    
    root2 = Node(1)
    node4 = Node(2)
    node5 = Node(3)
    
    root2.left = node4
    root2.right = node5
    
    print(sameTree(root1, root2))
    print(sameTree1(root1, root2))
    #----------
    
    root1 = Node(1)
    node2 = Node(2)
    root1.left = node2

    root2 = Node(1)
    node3 = Node(2)
    root2.right = node3

    print(sameTree(root1, root2))
    print(sameTree1(root1, root2))
    
