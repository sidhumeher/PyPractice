'''
Created on Nov 19, 2020

@author: sidteegela
'''


def strstr(hay, needle):
    
    if len(hay) == 0 and len(needle) == 0:
        return 0
    elif len(hay) == 0:
        return -1
    elif len(needle) == 0:
        return 0
    
    len_n = len(needle)
    len_h = len(hay)
    
    for item in range(len_h - len_n + 1):
        if needle[0] == hay[item]:  # Only proceed if the first char is same in hay and needle
            if needle == hay[item:item + len_n]:
                return item
                
    return -1
# Time complexity: O((len_h-len_n) * len_n)
# Space: O(1)


if __name__ == '__main__':
    hay = 'hello'
    needle = 'll'
    print(strstr(hay, needle))
    
    hay = 'aaaaaa'
    needle = 'bba'
    print(strstr(hay, needle))
    
    hay = ''
    needle = ''
    print(strstr(hay, needle))
    
    hay = 'aaababababaccceadd'
    needle = 'cce'
    print(strstr(hay, needle))
    
    hay = ''
    needle = 'c'
    print(strstr(hay, needle))
    
    hay = 'a'
    needle = 'a'
    print(strstr(hay, needle))
