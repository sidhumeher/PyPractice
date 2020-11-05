'''
Created on Nov 4, 2020

@author: sidteegela
'''
from collections import deque


def isValid(s):
    
    if len(s) == 0:
        return True
    
    mapping = {')':'(', ']':'[', '}':'{'}
    stack = deque()
    
    for item in s:
        if item in ['{', '[', '(']:
            # print('Inside append')
            stack.append(item)
        elif item in ['}', ']', ')']:
            poppedItem = stack.pop() if len(stack) != 0 else '*'
            if poppedItem != mapping[item]:
                # print('Inside 2nd if')
                return False
    # print(stack)
    if len(stack) == 0:
        return True
    
# Time complexity:O(n)
# Space: O(n) worst case if we push all braces onto stack


if __name__ == '__main__':
    # s = '()' #True
    # s = "()[]{}" #True
    # s = "(]"  # False
    # s = "([)]"  # False
    # s = '{[]}'  # True
    s = ']'
    print(isValid(s))
