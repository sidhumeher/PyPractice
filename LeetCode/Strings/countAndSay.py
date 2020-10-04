'''
Created on May 11, 2020

@author: sidteegela
'''
import itertools

def countAndSay(n):
    result = '1'
    '''
    for _ in range(n-1):
        v = ''
        for digit,group in itertools.groupby(result):
            count = len(list(group)
            v += "%i%s" % (count,digit)
        result += v
    '''
    return result
if __name__ == '__main__':
    
    n = 5
    print(countAndSay(n))