'''
Created on Dec 9, 2020

@author: sidteegela
'''


def reverseVowels(s):
    
    if len(s) == 0:
        return None
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newStr = list(s)
    p = 0; q = len(newStr) - 1
    
    while p <= q:
        while p < len(newStr) and newStr[p] not in vowels:
            p += 1
        while q >= 0 and newStr[q] not in vowels:
            q -= 1
        
        if p < q:
            newStr[q], newStr[p] = newStr[p], newStr[q]
            p += 1; q -= 1
        
    return ''.join(newStr)


if __name__ == '__main__':
    s = 'hello'
    print(reverseVowels(s))
    
    s = 'bcdr'
    print(reverseVowels(s))
