'''
Created on Oct 14, 2020

@author: sidteegela
'''
import collections

'''
Technique: Create a defaultdict with list as value
Read each string from InputList and sort it and use it as key sorted(str)
Ex: eat will be ('a','e','t')
Append each str as value to corresponding key and return dictioary values
'''


def groupAnagrams(strs):

    if len(strs) == 0:
        return []
    if len(strs) == 1:
        return strs
    
    trackingDict = collections.defaultdict(list)
    
    for str in strs:
        trackingDict[tuple(sorted(str))].append(str)
    
    print(trackingDict.values())
    

if __name__ == '__main__':
    
    inputList = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # inputList = ["eat", "tea"]
    groupAnagrams(inputList)
