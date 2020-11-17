'''
Created on Nov 2, 2020

@author: sidteegela
'''

# Diameter of a Binary search tree
# Or width of tree


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def diameter(node):
    
    if node == None:
        return 0
    
    result = 0
    
    def depth(node):
        nonlocal result
        if node == None:
            return 0
        
        left = depth(node.left)
        right = depth(node.right)
        
        result = max(result, left + right)  # Diameter of tree
        return max(left, right) + 1  # Max depth of node not diameter
        
    depth(node)
    return result

# Time complexity: O(n)

'''
Max of the following
1. Height of left+right subtree
2. Diameter of left subtree
3. Diameter of right subtree
max(l+r, max(ldiamter, rdiameter))
'''


def diameter1(node):
    if node == None:
        return 0
     
    def dfs(node):
        nonlocal result
        if node == None:
            return 0
        # Heights of left and right subtrees
        left = dfs(node.left)
        right = dfs(node.right)
    
        result = max(result, left + right)
        return max(left + 1, right + 1)
    
    result = 0
    dfs(node)
    return result


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
    
    # print(diameter(root))
    print(diameter1(root))
