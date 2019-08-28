'''
Created on Dec 31, 2018

@author: siddardha.teegela
'''

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if s[::-1] == s:
        return -1
    #substr = ''
    for index in range(0,len(s)):
        #substr = ""
        if index == 0:
            substr1 = ""
            substr1 = s[index+1:]
            print('Inside first if',substr1)
            if substr1[::-1] == substr1:
                return index
        else:
            substr2 = ""
            substr2 = s[:index]+s[index+1:]
            print('Inside second if',substr2)
            print('rev',substr2[::-1])
            if substr2[::-1] == substr2:
                return index
        
    return -1

if __name__ == '__main__':
        result = palindromeIndex('aaab')
        print(result)
        '''
        result = palindromeIndex('baa')
        print(result)
        result = palindromeIndex('aaa')
        print(result)
        '''