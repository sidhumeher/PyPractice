'''
Created on Jan 6, 2019

@author: siddardha.teegela
'''

def gameOfThrones(s):
    '''
    ip = dict()
    
    for char in s:
        if char in ip:
            ip.update({char:ip[char]+1})
        else:
            ip.update({char:1})
        
    count = 0    
    for v in ip.values():
        if v == 1:
            count += 1
    print('Count', count)
    if count <= 2:
        return 'YES'
    else:
        return 'NO'
    return 'NO'
    '''
    ip = dict()
    
    for char in s:
        if char in ip:
            ip.update({char:ip[char]+1})
        else:
            ip.update({char:1})
        
    '''
    Logic:
    If len(str) is even, count of each element should be even.
    If len(str) is odd, count of ONLY one element should be odd, counts of all other elements should be even
    '''        
    count = 0
    if s.__len__() / 2 == 0:
        for v in ip.values():
            if v % 2 != 0:
                count += 1
        if count == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        for v in ip.values():
            if v % 2 != 0:
                count += 1
        if count == 1:
            return 'YES'
        else:
            return 'NO'
    
    
if __name__ == '__main__':
    s = 'aaabbbb'
    result = gameOfThrones(s)
    print(result)
    
    s = 'cdefghmnopqrstuvw'
    result = gameOfThrones(s)
    print(result)
    
    s = 'cdcdcdcdeeeef'
    result = gameOfThrones(s)
    print(result)