'''
Created on Nov 11, 2020

@author: sidteegela
'''


def sortedSquares(A):
    
    if len(A) == 0:
        return
    
    for i in range(len(A)):
        A[i] = A[i] * A[i]  # squares of item
    
    A.sort()
    return A

# Time Complexity: O(n logn)
# Space: O(1)


# Better approach
def sortedSquares1(A):
    
    if len(A) == 0:
        return
    
    result = [0] * len(A)
    
    left = 0; right = len(A) - 1
    while left <= right:
        A[left], A[right] = abs(A[left]), abs(A[right])
        # print(A[left])
        # print(A[right])
        if A[left] > A[right]:
            result[right - left] = A[left] * A[left]
            left += 1
        else:
            result[right - left] = A[right] * A[right]
            right -= 1
            
    return result
# Time: O(n)
# Space: O(n)


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    # print(sortedSquares(A))
    print(sortedSquares1(A))
    
    A = [-7, -3, 2, 3, 11]
    # print(sortedSquares(A))
    print(sortedSquares1(A))
