'''
Created on Jul 10, 2019

@author: siddardha.teegela
'''

from DataStructures.Stack import Stack

'''
Given a string of brackets, determine if the string is balanced

Sample Input
{[()]}
{[(])}
{{[[(())]]}}

Sample Output
YES
NO
YES
'''

def is_balanced(ip):
    s = Stack()
    match_pair = {')':'(',']':'[','}':'{'}
    
    for item  in ip:
        if item == '{' or item == '(' or item == '[':
            s.push(item)
        else:
            if match_pair[item]== s.peak():
                s.pop()
            else:
                return False
    '''
    Return True if stack is empty, False otherwise
    '''
    return not s.size()

if __name__ == '__main__':
    result = is_balanced('{[()]}')
    print(result)
    
    result = is_balanced('{[(])}')
    print(result)
    
    result = is_balanced('{{[[(())]]}}')
    print(result)