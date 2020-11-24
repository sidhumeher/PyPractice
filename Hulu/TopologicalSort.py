'''
Created on Nov 23, 2020

@author: sidteegela
'''
from _collections import defaultdict


class Graph:
    
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def tsUtil(self, v, visited, stack):
        
        visited[v] = True
        
        # Recurse all vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.tsUtil(i, visited, stack)
        # Push current vertex to stack
        stack.insert(0, v)

    def topologicalSort(self):
        
        # Mark all vertices as not visited
        visited = [False] * self.vertices
        stack = []
        
        for i in range(self.vertices):
            if visited[i] == False:
                self.tsUtil(i, visited, stack)
        print(stack)
        # Time complexity: O(v+e),v=no of vertices, e=no of edges
        # Space: O(v)


if __name__ == '__main__':
    
    g = Graph(6) 
    g.addEdge(5, 2); 
    g.addEdge(5, 0); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1);
     
    g.topologicalSort()
    
    # print(g.graph)
