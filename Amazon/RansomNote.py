'''
Created on Dec 9, 2020

@author: sidteegela
'''


def canConstruct(ransom, maganize):
    
    if len(maganize) == 0:
        return False
    
    magTracker = {}
    
    for item in maganize:
        if item not in magTracker:
            magTracker[item] = 1
        else:
            magTracker[item] += 1
            
    # iterate through ransom note
    for item in ransom:
        if item not in magTracker or magTracker[item] == 0:
            return False
        else:
            magTracker[item] -= 1

    return True


if __name__ == '__main__':
    ransom = 'a'; magazine = 'b'
    print(canConstruct(ransom, magazine))
    
    ransom = 'aa'; magazine = 'ab'
    print(canConstruct(ransom, magazine))
    
    ransom = 'aa'; magazine = 'aab'
    print(canConstruct(ransom, magazine))
