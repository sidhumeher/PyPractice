'''
Created on Nov 30, 2020

@author: sidteegela
'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(node):        
    
    if node == None:
        return 0

    maxsum = float('-inf')
    
    def helper(node):
        
        nonlocal maxsum
        if node == None:
            return 0
        
        leftGain = max(helper(node.left), 0)  # 0 because we can return 0 if left child is negative
        rightGain = max(helper(node.right), 0)  # same as above
        
        currentMax = node.val + leftGain + rightGain
        maxsum = max(maxsum, currentMax)
        
        return node.val + max(leftGain, rightGain)  # we only consider left or right node+current node
    
    helper(root)
    return maxsum

# Time: O(n)
# Space: O(1)

                
if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    
    root.left = node1
    root.right = node2
    
    print(maxPathSum(root))
    
    #########
    
    root = TreeNode(-10)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    
    print(maxPathSum(root))
