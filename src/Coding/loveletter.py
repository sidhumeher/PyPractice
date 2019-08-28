'''
Created on Jan 5, 2019

@author: siddardha.teegela
'''
def theLoveLetterMystery(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    inputAsList = list(s)
    #inputAsString = "".join(inputAsList)
    result = 0
    start = 0
    end = s.__len__()-1
    
    while True:
        if s[::-1] == s:
            break
            #return result
        if inputAsList[start] == inputAsList[end]:
            start += 1
            end -= 1
        if inputAsList[start] < inputAsList[end]:
            index = alphabet.index(inputAsList[end])
            inputAsList[end] = alphabet[index-1]
            print(inputAsList)
            result += 1
        elif inputAsList[start] > inputAsList[end]:
            index = alphabet.index(inputAsList[start])
            inputAsList[start] = alphabet[index-1]
            print(inputAsList)
            result += 1
        if start == end or start > end:
            break
    
    return result
    

if __name__ == '__main__':
    s = 'abc'
    result = theLoveLetterMystery(s)
    #print(result)
    
    s = 'abcba'
    result = theLoveLetterMystery(s)
    print(result)
    
    s = 'abcd'
    result = theLoveLetterMystery(s)
    print(result)
    
    s = 'cba'
    result = theLoveLetterMystery(s)
    print(result)