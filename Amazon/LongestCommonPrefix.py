'''
Created on Dec 9, 2020

@author: sidteegela
'''


def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ''
    
    result = ''
    
    index = 0
    while index < len(strs[0]):
        compareChar = strs[0][index]
        for item in strs[1:]:
            if compareChar != item[index]:
                return result
        result += compareChar
        index += 1
        
    return result

# Time complexity: O(n^2)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
    
    strs = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs))
    
    strs = ['leets', 'leetcode', 'leetc', 'leeds']
    print(longestCommonPrefix(strs))
