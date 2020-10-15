'''
Created on Oct 14, 2020

@author: sidteegela
'''


def multiply(str1, str2):
    
    result = [0] * (len(str1) + len(str2))
    resultPosition = len(result) - 1
    
    for i in reversed(str1):
        tempPosition = resultPosition
        
        for j in reversed(str2):
            result[tempPosition] += int(i) * int(j)
            result[tempPosition - 1] += result[tempPosition] // 10
            result[tempPosition] %= 10
            tempPosition -= 1
        
        resultPosition -= 1
        
    # Removing any 0 padding before the result
    zeroPointer = 0
    while zeroPointer < len(result) - 1 and result[zeroPointer] == 0:
        zeroPointer += 1
    
    print(''.join(map(str, result[zeroPointer:])))


if __name__ == '__main__':
    
    result = multiply('123', '456')
