'''
Created on Nov 18, 2020

@author: sidteegela
'''


def compareVersion(v1, v2):
    
    if len(v1) == 0 and len(v2):
        return -1
    elif len(v1) and len(v2) == 0:
        return 1
    
    v1_list = v1.split('.')
    v2_list = v2.split('.')
    
    len1 = len(v1_list)
    len2 = len(v2_list)
    
    if len1 > len2:
        v2_list = v2_list + ['0'] * (len1 - len2)
    elif len2 > len1:
        v1_list = v1_list + ['0'] * (len2 - len1)

    index = 0
    
    for index in range(len(v1_list)):
        if int(v1_list[index]) > int(v2_list[index]):
            # print('>')
            return 1
        elif int(v1_list[index]) < int(v2_list[index]):
            # print('<')
            return -1
        elif int(v1_list[index]) == int(v2_list[index]):
            # print('==')
            continue

    return 0

# Time complexity: O(n)
# Space complexity: O(n+m),n=length of v1list and m=length of v2list


if __name__ == '__main__':
    v1 = '7.5.2.4'
    v2 = '7.5.3'
    print(compareVersion(v1, v2))
    
    v1 = '1.0.1'
    v2 = '1'
    print(compareVersion(v1, v2))
    
    v1 = '0.1'
    v2 = '1.1'
    print(compareVersion(v1, v2))
    
    v1 = '1.0'
    v2 = '1.0.0'
    print(compareVersion(v1, v2))
    
    v1 = '1.01'
    v2 = '1.001'
    print(compareVersion(v1, v2))
    
    v1 = '1'
    v2 = '1.1'
    print(compareVersion(v1, v2))
