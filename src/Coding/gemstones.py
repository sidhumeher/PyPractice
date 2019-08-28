'''
Created on Jan 5, 2019

@author: siddardha.teegela
'''


def gemstones(arr):
    result = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z']
    alphIndex = 0
    while alphIndex < alphabet.__len__():
        alphcount = 0
        for item in arr:
            if alphabet[alphIndex] in item:
                alphcount +=1
        if alphcount == arr.__len__():
            result += 1
        
        alphIndex +=1
    return result

if __name__ == '__main__':
    arr = ['abcdde','baccd','eeabg']
    result = gemstones(arr)
    print(result)
