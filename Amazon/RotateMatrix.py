'''
Created on Oct 22, 2020

@author: sidteegela
'''

# Technique: Transpose and then reverse
# Time Complexity: O(n ^ 2)


def rotateMatrix(ipList):
    if len(ipList) == 0:
        return
    
    n = len(ipList[0])
    # Transpose
    for i in range(n):
        for j in range(i, n):
            ipList[j][i], ipList[i][j] = ipList[i][j], ipList[j][i]
        
    # Reverse
    for item in range(len(ipList)):
        ipList[item].reverse()

    print(ipList)


if __name__ == '__main__':
    
    ipList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateMatrix(ipList)
