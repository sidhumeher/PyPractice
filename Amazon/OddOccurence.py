'''
Created on Oct 21, 2020

@author: sidteegela
'''


def oddItem(ipList):
    
    if len(ipList) == 0:
        return

    countDict = {}
    
    for item in ipList:
        if item not in countDict:
            countDict[item] = 1
        else:
            countDict[item] += 1
            
    for key, value in countDict.items():
        
        if value % 2 != 0:
            print(key)
            

if __name__ == '__main__':
    
    ipList = [1, 2, 3, 2, 3, 1, 3]
    oddItem(ipList)
