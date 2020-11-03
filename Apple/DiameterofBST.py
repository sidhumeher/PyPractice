'''
Created on Nov 2, 2020

@author: sidteegela
'''

# Diameter of a Binary search tree


def diameter(node):
    
    if node == None:
        return 0
    
    result = 0
    
    def depth(node):
        
        if node == None:
            return 0
        
        left = depth(node.left)
        right = depth(node.right)
        
        result = max(result, left + right)  # Diameter of tree
        return max(left, right) + 1  # Max depth of node not diameter
        
    depth(node)
    return result

# Time complexity: O(n)


if __name__ == '__main__':
    pass
