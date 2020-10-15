'''
Created on Oct 13, 2020

@author: sidteegela
'''


def checkIfValid(str):
    openCount = 0
    closeCount = 0
    
    for item in str:
        if item == '(':
            openCount += 1
        if item == ')':
            closeCount += 1

    if openCount == closeCount:
        return True
    else:
        return False


def invalidParantheses(inputString):
    
    if inputString == '':
        return None


if __name__ == '__main__':
    
    print(invalidParantheses('()())()'))
