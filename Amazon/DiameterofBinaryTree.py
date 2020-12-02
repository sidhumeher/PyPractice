'''
Created on Dec 1, 2020

@author: sidteegela
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameterofBinaryTree(node):
    result = 1
    if node == None:
        return 0
    
    def helper(node):
        nonlocal result
        if node == None:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        result = max(result, left + right)
        return max(left, right) + 1
    
    helper(node)
    return result

# Time complexity:O(n)
# Space: O(n) for call stack


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    
    root.left = node1
    root.right = node2
    
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    
    node1.left = node3
    node1.right = node4
    
    print(diameterofBinaryTree(root))
    
