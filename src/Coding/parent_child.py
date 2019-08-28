'''
Created on Nov 30, 2018

@author: siddardha.teegela
'''
# Suppose we have some input data describing a graph of relationships between parents and children 
#over multiple generations. The data is formatted as a list of (parent, child) pairs, where each 
#individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
            
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   10

# Write a function that takes this data as input and returns two collections: 
#one containing all individuals with zero known parents, and 
#one containing all individuals with exactly one known parent.

# Sample output (pseudodata):
# [
#   [1, 2, 4],   // Individuals with zero parents
#   [5, 7, 8, 10] // Individuals with exactly one parent
# ]

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10)
]


def parent_child(parent_child_pairs):
    noParent = []
    
    for pair in parent_child_pairs:
        checked = False
        for second in parent_child_pairs:
            if pair[0] != second[1]:
                continue
            else:
                checked = True
                #noParent.append(pair[0])
        if checked == False:
            noParent.append(pair[0])
    
    print(set(noParent)) # No parents
    
    oneParentDict = dict()
    oneParentList = []
    
    for pair in parent_child_pairs:
        if pair[1] in oneParentDict:
            #value = oneParent[pair[1]]
            kv = {pair[1]: oneParentDict[pair[1]]+1}
            oneParentDict.update(kv)
        else:
            oneParentDict.update({pair[1]:1})
            
    for key in oneParentDict.keys():
        if oneParentDict[key] == 1:
            oneParentList.append(key)
    
    print(oneParentList)
        
parent_child(parent_child_pairs)        