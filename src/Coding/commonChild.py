'''
Created on Jan 2, 2019

@author: siddardha.teegela
'''

def commonChild(s1, s2):
    dict1 = dict()
    
    for char in s1:
        if char in dict1:
            dict1.update({char:dict1[char]+1})
        else:
            dict1.update({char:1})
            
    count = 0
    for char in s2:
        if char in dict1:
            if not dict1[char] == 0:
                count +=1
                dict1.update({char:dict1[char]-1})
        else:
            continue
    return count

if __name__ == '__main__':
    s1 = 'HARRY'
    s2 = 'SALLY'
    result = commonChild(s1, s2)
    print(result)
    
    s1 = 'SHINCHAN'
    s2 = 'NOHARAAA'
    result = commonChild(s1, s2)
    print(result)
    
    s1 = 'ABCDEF'
    s2 = 'FBDAMN'
    result = commonChild(s1, s2)
    print(result)