'''
Created on May 20, 2019

@author: siddardha.teegela

'''

def appendAndDelete(s, t, k):
    if s == t:
        return 'Yes'

    checkIndex = 0
    lenOfS = len(s)
    lenOfT = len(t)

    while(True):
        if lenOfS > 0 and lenOfT > 0 and s[checkIndex] == t[checkIndex]:
            print('Inside If')
            checkIndex += 1
            lenOfS -= 1
            lenOfT -= 1
            print('lenS', lenOfS)
            print('lenT', lenOfT)
            print(checkIndex)
        else:
            print('Inside Else')
            break

    newS = s[checkIndex:]
    newT = t[checkIndex:]

    if len(newS) + len(newT) > k :
        return 'No'
    else:
        k -= len(newS)
        newS = s[:checkIndex]

    for character in newT:
        newS += character
        k -= 1

    print(newS)
    # print(newT)

    if newS == t:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    s = 'hackerhappy'
    t = 'hackerrank'
    k = 9
    result = appendAndDelete(s, t, k)
    print(result)
