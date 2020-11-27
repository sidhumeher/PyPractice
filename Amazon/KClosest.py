'''
Created on Nov 26, 2020

@author: sidteegela
'''
# K closest points to origin

import math


def kClosest(points, k):

    def distance(p):
        distance = math.sqrt((p[0] ** 2) + (p[1] ** 2))
        return distance
    
    points.sort(key=lambda p:distance(p))
    print(points)
    
    return points[:k]

# Time complexity :O(n log n)
# Space: O(n)


if __name__ == '__main__':
    k = 1
    points = [[1, 3], [-2, 2]]
    print(kClosest(points, k))
    
    k = 2
    points = [[3, 3], [5, -1], [-2, 4]]
    print(kClosest(points, k))
    
    k = 2
    points = [[1, 3], [-1, 3], [1, -3], [-1, -3]]
    print(kClosest(points, k))
    
    k = 2
    points = [[-5, 4], [-6, -5], [4, 6]]
    print(kClosest(points, k))
