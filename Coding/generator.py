'''
Created on Mar 3, 2019

@author: siddardha.teegela
'''

def generateNum(n):
    num = 0
    
    while num < n:
        yield num
        num +=1

if __name__ == '__main__':
    print(sum(generateNum(5)))
    print(list(generateNum(5)))