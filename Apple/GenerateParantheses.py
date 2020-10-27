'''
Created on Oct 26, 2020

@author: sidteegela
'''


def generateParanteses(n):
    
    if n == 0:
        return []
    
    result = []
    
    def generateHelper(A=[]):
        if len(A) == 2 * n:
            if valid(A):
                result.append((''.join(A)))
        else:
            A.append('(')
            generateHelper(A)
            A.pop()
            A.append(')')
            generateHelper(A)
            A.pop()
        
    def valid(A):
        balance = 0
        for item in A:
            if item == '(':
                balance += 1
            else:
                balance -= 1
        if balance < 0:
            return False
        return balance == 0

    generateHelper()
    print(result)


def generateParanthesis_recursion(n):
    result = []
    
    def helper(s='', left=0, right=0):  # Backtracking
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:  # If left less than n, add '(        
            helper(s + '(', left + 1 , right)
        if right < left:  # Add ')' if right brackets count is less than left count
            helper(s + ')', left, right + 1)
    
    helper()
    print(result)


if __name__ == '__main__':
    n = 2
    generateParanteses(n)
    
    n = 2
    generateParanthesis_recursion(n)
    n = 3
    generateParanthesis_recursion(n)
