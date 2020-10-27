'''
Created on Oct 22, 2020

@author: sidteegela
'''

# Find the maximum path sum.
# The path must contain at least one node and does not need to go through the root.


def maxPathSum(self, root):
        
    def max_gain(node):
        nonlocal max_sum
            
        if node == None:
            return 0
            
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
            
        price_newpath = node.val + left_gain + right_gain
    
        max_sum = max(max_sum, price_newpath)
            
        return node.val + max(left_gain, right_gain)
        
    max_sum = float('-inf')
    max_gain(root)
    return max_sum


if __name__ == '__main__':
    pass
