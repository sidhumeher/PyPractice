'''
Created on Feb 16, 2019

@author: siddardha.teegela
'''

if __name__ == '__main__':
    #s = input()
    s = 'qA2'
    
    '''
    Use of any() and built in str functions
    '''
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))