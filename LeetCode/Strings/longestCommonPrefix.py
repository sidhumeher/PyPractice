'''
Created on May 11, 2020

@author: sidteegela
'''

def longestCommonPrefix(inputList):
    
    if len(inputList) == 0:
        return ""
    
    result = ''
    search = list(inputList[0])
    
    index = 0
    while index < len(search):
        count = 0
        for word in inputList:
            if index < len(word) and search[index] == word[index]:
                count += 1
        if count == len(inputList):
            result += search[index]
            index += 1
        else:
            break

    if result != '':
        return result
    else:
        return ""
    
# Run time: 40 MS
# Memory Usage: 13.9 MB

if __name__ == '__main__':
    
    inputList = ["flower","flow","flight"]
    print(longestCommonPrefix(inputList))
    
    inputList = ["dog","racecar","car"]
    print(longestCommonPrefix(inputList))
    
    inputList = ["aa","a","aaa"]
    print(longestCommonPrefix(inputList))