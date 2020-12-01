'''
Created on Nov 27, 2020

@author: sidteegela
'''
from queue import Queue


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(node):
    
    if node == None:
        return []
    
    result = []; level = 0
    q = Queue()
    
    q.put_nowait(node)
    
    # Generating level order of nodes
    while not q.empty():
        result.append([])
        
        for _ in range(q.qsize()):
            node = q.get_nowait()
            result[level].append(node.val)
            
            if node.left:
                q.put_nowait(node.left)
            if node.right:
                q.put_nowait(node.right)
        level += 1
        
    # Reversing nodes in alternate levels
    index = 0
    while index < len(result):
        if index % 2 != 0:
            result[index].reverse()
        index += 1
    
    return result

# Time complexity: O(n+time to reverse nodes of odd levels)
# Space: O(n)


if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    
    print(levelOrder(root))
    
    ###########
    
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    
    root.left = node2
    root.right = node3
    
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    print(levelOrder(root))
