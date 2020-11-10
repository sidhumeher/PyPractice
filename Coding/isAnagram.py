'''
Created on Dec 3, 2018

@author: siddardha.teegela
'''
def is_anagram(ip1,ip2):
    ip1Dic = dict()
    ip2Dic = dict()
    
    # Put each alphabet as key and no of occurences as value
    for c in ip1:
        if c in ip1Dic:
            ip1Dic.update({c:ip1Dic[c]+1})
        else:
            ip1Dic.update({c:1})
            
    for c in ip2:
        if c in ip2Dic:
            ip2Dic.update({c:ip2Dic[c]+1})
        else:
            ip2Dic.update({c:1})
            
    # Flag to check anagram
    isAnagram = False
    
    # Check if each alphabet in both strings occur equal no of times. If yes then print True or else False(Not Anagrams)
    for key in ip1Dic.keys():
        #print(ip1Dic[key])
        #print(ip2Dic[key])
        if not ip2Dic.__contains__(key):
            isAnagram = False
            print ('False')
            break
        elif ip1Dic[key] == ip2Dic[key]:
            isAnagram = True
            continue
        else:
            isAnagram = False
            print ('False')
            break
        
    if isAnagram == True:
        print ('True')
    
    
is_anagram('hello','helol')
is_anagram('ltpo', 'pot')