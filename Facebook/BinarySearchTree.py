'''
Created on Oct 12, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
class BST(object):
    
    def __init__(self):
        self.root = None
        
    # Left->Root->Right
    def inOrder(self):
        resultArary = []
        
        if self.left:
            return self.left.inOrder()
        resultArary.append(self.left.data)
        
        if self.right:
            return self.right.inOrder()

        return resultArary

    # Left->Right->Root
    def postOrder(self):
        resultArray = []
        if self.left:
            return self.left.postOrder()
        if self.right:
            return self.right.postOrder()
        resultArray.append(self.data)
        
        return resultArray
    
    # Root->Left->Right
    def preOrder(self):
        resultArray = []
        
        resultArray.append(self.data)
        
        if self.left:
            return self.left.preOrder()
        if self.right:
            self.right.preOrder()
            
        return resultArray
    
    '''
    For Inorder,PreOrder,PostOrder Time Complexity: O(n)
    n = No of nodes
    Space Complexity: O(n) to store in array or else O(1)
    Functional call stack reaches a depth of h, height of tree O(h)
    '''

    def height(self, root):
        
        # Base condition
        if root is None:
            return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):  # Time complexity O(n^2)
        
        # Base condition
        if root is None:
            return True
        
        left_subtree = self.height(root.left)
        right_subtree = self.height(root.right)

        # Accepted values for height difference are -1,0,1
        if abs(left_subtree - right_subtree) <= 1 and self.isBalanced(root.left) == True and self.isBalanced(root.right):
            return True
            
        return False

    def isBalanced2(self, root):  # Better solution. Time: O(n)
       
        def helper(root):
            
            if root == None:
                return 0
            
            left_height = self.helper(root.left)
            if left_height == -1:
                return -1
            right_height = self.height(root.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
         
        if helper(root) > -1:
            return True

    def isSymmetric(self, root):  # Time Complexity: O(n)
        
        if root == None:
            return True

        def helper(node1, node2):
            
            if node1 == None and node2 == None:
                return True
            else:
                if node1.data != node2.data:
                    return False
                else:
                    return helper(node1.left, node2.right) and helper(node1.right, node2.left)
                
            return False

        return helper(root.left, root.right)


if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # root.right.left = Node(6)
    
    root.left.left.left = Node(8)
    
    bst = BST()
    bst.root = root
    
    if bst.isBalanced(root):
        print('Tree is balanced')
    else:
        print('Tree is not balanced')
    
