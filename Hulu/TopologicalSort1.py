'''
Created on Nov 23, 2020

@author: sidteegela
'''


def helper(key, visited, stack):
    
    visited[key] = True
    
    if key not in graph:
        # print('Inside if')
        stack.insert(0, key)
        return
    for node in graph[key]:
        # print('Inside for')
        if node not in visited:
            helper(node, visited, stack)
    stack.insert(0, key)


def topologicalSort(graph):
    visited = {}
    stack = []
    
    for key, value in graph.items():
        if key not in visited:
            helper(key, visited, stack)
    
    print(stack)


if __name__ == '__main__':
    graph = {5:[0, 2], 4:[0, 1], 2:[3], 3:[1]}
    topologicalSort(graph)
