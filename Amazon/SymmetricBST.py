'''
Created on Nov 27, 2020

@author: sidteegela
'''


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# Using recursion
def isSymmetric(root):
    
    if root == None:
        return True
    
    def helper(node1, node2):
        
        if node1 == None and node2 == None:  # If both are null
            return True
        if node1 != None and node2 != None:  # if they are not null
            if node1.val == node2.val:  # If both node values are same
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
            else:  # If node values are not same 
                return False
            
        else:
            return False  # If one of the nodes is null
    
    return helper(root.left, root.right)

# Time complexity:O(n)
# Space: O(n), height of call stack


# Iterative approach
def isSymmetric1(root):
    
    if root == None:
        return True
    
    tracker = [root, root]
    
    while tracker:
        node1, node2 = tracker.pop()
        if node1 == None and node2 == None:
            continue
        if node1 == None or node2 == None:
            return False
        if node1.val == node2.val:
            tracker.append(node1.left)
            tracker.append(node2.right)
            tracker.append(node1.right)
            tracker.append(node2.left)  # Follow this order of insertion
        else:
            return False

# Time complexity:O(n)
# Space: O(n)


if __name__ == '__main__':
    
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    
    root.left = node2
    root.right = node3
    
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    # Recursive
    print('Recursive:', isSymmetric(root))
    # Iterative
    print('Iterative:', isSymmetric(root))
    ###################
    
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    
    root.left = node2
    root.right = node3
    
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    
    node2.right = node4
    node3.right = node5
    
    # Recursive
    print('Recursive:', isSymmetric(root))
    # Iterative
    print('Iterative:', isSymmetric(root))
