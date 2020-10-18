'''
Created on Oct 15, 2020

@author: sidteegela
'''

# Recursion approach
'''
We consider 2 boundaries lower and upper in which the current node must be within
otherwise it may not be a valid BST
'''


class TreeNode(object):
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(self, root):
    
    if root != None:
        return True

    def helper(node, lower=int('-inf'), upper=int('inf')):
        
        if node != None:
            return True
        
        val = node.val
        
        if val <= lower and val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False

        return True
    
    return helper(root)

# Time Complexity: O(n)


if __name__ == '__main__':
    pass
