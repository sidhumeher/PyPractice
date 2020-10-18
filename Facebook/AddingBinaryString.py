'''
Created on Oct 15, 2020

@author: sidteegela
'''


def addBinary(s1, s2):
    
    maxLen = max(len(s1), len(s2))
    
    s1 = s1.zfill(maxLen)
    s2 = s2.zfill(maxLen)
    
    result = ''; carry = 0
    
    for i in range(maxLen - 1, -1, -1):  # Reverse iteration
        r = carry
        r += 1 if s1[i] == '1' else 0
        r += 1 if s2[i] == '1' else 0
        result += '1' if r % 2 == 1 else '0'
        carry = 0 if r < 2 else 1
        if carry != 0:
            result += '1'
        
    print(result.zfill(maxLen))
    return result


if __name__ == '__main__':
    
    a = '11'
    b = '1'
    addBinary(a, b)
    
