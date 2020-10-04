'''
Created on May 11, 2020

@author: sidteegela
'''

#Using find(). Returns first index of search string if found. Else return -1
def strstr(haystack,needle):
    if needle == '' or needle == ' ':
        return 0
    
    return haystack.find(needle)
    

if __name__ == '__main__':
    
    haystack = 'hello'
    needle = 'll'
    print(strstr(haystack,needle))
    
    haystack = 'aaaaa'
    needle = 'bba'
    print(strstr(haystack,needle))