'''
Created on Oct 20, 2020

@author: sidteegela
'''

# Stack is the best data structure to use. Push to stack if it is open bracket, 
# check stack top and compare mapping and pop otherwise


def validParantheses(inputString):
    
    if len(inputString) == 0:
        return True
    
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}  # closer brackets as key and open brackets as value

    for item in inputString:
        if item in mapping:
            top_of_stack = stack.pop() if stack else '#'  # Else assign some dummy value
    
            if mapping[item] != top_of_stack:
                return False
        else:
            stack.append(item)
        
    if len(stack) != 0:
        return False
    else:
        return True
        
# Time complexity: O(n)
# Space complexity: O(n)        

        
if __name__ == '__main__':
    
    print(validParantheses('()'))
    print(validParantheses('()[]{}'))
    print(validParantheses('(]'))
    
