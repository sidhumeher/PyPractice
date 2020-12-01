'''
Created on Nov 26, 2020

@author: sidteegela
'''


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# User lower and upper limit technique
# Recursion method
def isValidBST(root):
    
    if root == None:
        return True
    
    def helper(node, low, high):
        
        if node == None:
            # print('Inside first if')
            return True
        
        if node.val < low or node.val > high:
            return False
        
        # print(node.val)
        value = node.val
        if helper(node.left, low, value) != True:
            return False
        if helper(node.right, value, high) != True:
            return False
            
        return True
    
    low = float('-inf')
    high = float('inf')
    return helper(root, low, high)

# Time complexity: O(n)
# Space: O(n), call stack size


# Iteration method
# Using stack and DFS
def isValidBST1(root):
    
    if root == None:
        return True
    
    stack = [(root, float('-inf'), float('inf'))]
    
    while stack:
        root, lower, upper = stack.pop()
        if root == None:
            continue
        
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.left, lower, val))
        stack.append((root.right, val, upper))
        
    return True

# Time complexity: O(n)
# Space: O(n)


if __name__ == '__main__':
    root = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    
    root.left = node1
    root.right = node2
    
    print(isValidBST(root))
    
    #########
    
    root = TreeNode(5)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    
    root.left = node1
    root.right = node2
    
    node3 = TreeNode(3)
    node4 = TreeNode(6)
    
    node2.left = node3
    node2.right = node4
    
    print(isValidBST(root))

