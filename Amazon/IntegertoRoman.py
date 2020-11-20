'''
Created on Nov 19, 2020

@author: sidteegela
'''


def inttoRoman(num):
    
    mapping = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', \
               50:'L', 40:'XL', 10:'X', 9:'IX', 8:'VIII', 7:'VII', 6:'V1', \
               5:'V', 4:'IV', 3:'III', 2:'II', 1:'I'}
    
    if num in mapping:
        return mapping[num]
    
    result = []
    
    for digit, symbol in mapping.items():
        if num == 0:
            break
        count, num = divmod(num, digit)
        result.append(symbol * count)
            
    return ''.join(result)

# Time complexity: O(n)
# Space: O(1)      


if __name__ == '__main__':
    num = 1994
    print(inttoRoman(num))
