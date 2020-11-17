'''
Created on Nov 16, 2020

@author: sidteegela
'''


def lowestCommonAncestor(root, p, q):

    result = None

    def recurse(node):
        if node == None:
            return False
        
        # left recursion
        left = recurse(node.left)
        # right recursion
        right = recurse(node.right)
        
        # if current node is p or q
        mid = node == p or node == q
        
        # if any of 2 of 3 flags are true
        if mid + left + right >= 2:
            result = node
        # return if either of 3 flags is true
        return mid or left or right
       
    recurse(root)
    return result

# Time complexity:O(n)
# Space: O(n), max length of recursive stack


if __name__ == '__main__':
    pass
