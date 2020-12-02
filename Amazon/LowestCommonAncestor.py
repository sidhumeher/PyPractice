'''
Created on Nov 30, 2020

@author: sidteegela
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursion method
def lowestCommonAncestor(root, p , q):

    if root == None:
        return False
    
    result = None
    
    def helper(node):
        
        if node == None:
            return False
        
        left = helper(node.left)
        right = helper(node.right)
        
        # If current node is p or q
        mid = node == p or node == q
            
        if mid + left + right >= 2 :
            result = node
        
        return mid or left or right
    
    helper(root)
    return result


# Iterative method
# Save parent nodes to dictionary
def lowestCommonAncestor1(root, p , q):
    
    # stack to traverse tree
    stack = [root]
    # Track parent of each node
    parent = {root:None}

    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    
    # add ancestors of p
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    
    # First ancestor of q which appears in p's ancestor is the common ancestor
    while q not in ancestors:
        q = parent[q]
    
    print(q.val)
    return q

# Time complexity: O(n)
# Space: O(n)


if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(7)
    node6 = TreeNode(4)
    node8 = TreeNode(0)
    node9 = TreeNode(8)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node4.left = node5
    node4.right = node6
    node2.left = node8
    node2.right = node9
    p = node1; q = node2
    
    # print(lowestCommonAncestor(root, p, q))
    print(lowestCommonAncestor1(root, p, q))
    
