'''
Created on Oct 22, 2020

@author: sidteegela
'''


def threeSum(ipList):
    
    result = []
    ipList.sort()
    
    for i in range(0, len(ipList) - 2):
        if i > 0 and ipList[i] == ipList[i - 1]:
            # Avoiding duplicates
            continue
        
        l = i + 1
        r = len(ipList) - 1
        
        # Two sum problem
        while l < r:
            sum = ipList[i] + ipList[l] + ipList[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.append([ipList[i], ipList[l], ipList[r]])
                # Avoiding duplicates
                while l < len(ipList) - 1 and ipList[l] == ipList[l + 1]:
                    l += 1
                while r > 0 and ipList[r] == ipList[r - 1]:
                    r -= 1
            l += 1; r -= 1
    
    return result


if __name__ == '__main__':
    ipList = [-1, 0, 1, 2, -1, -4]
    print(threeSum(ipList))
    
