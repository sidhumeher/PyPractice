'''
Created on Jan 4, 2019

@author: siddardha.teegela
'''

def morganAndString(a, b):
    
    if a.__len__() == 0:
        return b
    if b.__len__() == 0:
        return a
    
    aList = []
    bList = []
    result = ''
    
    for char in a:
        aList.append(char)
    
    for char in b:
        bList.append(char)
   
    aChar = 0
    bChar = 0
    
    while(True):
        
        if aList.__len__() == 0:
            for char in bList:
                result += char
            break
        elif bList.__len__() == 0:
            for char in aList:
                result += char
            break
                
        if aList[aChar] < bList[bChar] or aList[aChar] == bList[bChar]:
            result += aList[aChar]
            aList.remove(aList[aChar])
        else:
            result += bList[aChar]
            bList.remove(bList[bChar])
    
    return result
    

if __name__ == '__main__':
    a = 'JACK'
    b = 'DANIEL'
    result = morganAndString(a, b)
    print(result)
    
    a = 'YZYYZYZYY'
    b = 'ZYYZYZYY'
    result = morganAndString(a, b)
    print(result)