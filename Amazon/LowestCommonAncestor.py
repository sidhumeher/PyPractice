'''
Created on Nov 30, 2020

@author: sidteegela
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p , q):

    if root == None:
        return True
    
    if root == p or root == q:
        return True


if __name__ == '__main__':
    p = 0; q = 0
    
