'''
Created on Oct 21, 2020

@author: sidteegela
'''

from itertools import permutations

# Using built in permutation() method


def permutation_usingbuiltin(inputString):
    permutationList = permutations(inputString)
    for item in list(permutationList):
        print(''.join(item))

# Using recursion and backtracking technique


def permutation(inputString, step=0):
    
    if step == len(inputString):
        # we have reached the end of permutation. Print it
        print(''.join(inputString))
        
    for i in range(step, len(inputString)):
        
        # Copy input and store as list
        copyInput = [i for i in inputString]
        print(copyInput)
        # Swap current i with step
        copyInput[i], copyInput[step] = copyInput[step], copyInput[i]
        # Recurse on portion of string that is not swapped yet
        permutation(copyInput, step + 1)


if __name__ == '__main__':
    inputString = 'ABC'
    # permutation_usingbuiltin(inputString)
    permutation(inputString)
