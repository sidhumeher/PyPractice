'''
Created on Nov 11, 2020

@author: sidteegela
'''
# Clone a graph and return the reference to clone


class Node(object):
    
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is None else []


visited = {}


# Using recursion
def cloneGraph(node):
    
    if node == None:
        return None

    if node in visited:
        return visited[node]
    
    clone = Node(node.val, [])
    visited[node] = clone
    
    if node.neighbors:
        for node in node.neighbors:
            clone.neighbors.append(cloneGraph(node))
    
    return clone
        

if __name__ == '__main__':
    pass
