'''
Created on Jan 17, 2019

@author: siddardha.teegela
'''

def desc(s):
    words_split = s.split(" ")
    #print(words_split)
    words = dict()
    for w in words_split:
        if w in words:
            words.update({w:words[w]+1})
        else:
            words.update({w:1})
    
    print(words)

    
    demoList =  [(words[k], k) for k in words]
    '''
    demoList = []
    for k in words:
        demoList.append((words[k],k))
    '''
    print(sorted(demoList,reverse=True))
    
    #print(sortList.sort(reverse=True))

if __name__ == '__main__':
    s = 'siddardha guna sid guna siddardha guna'
    desc(s)
    s = 'guna guna'
    #desc(s)
    s = ''
    s = '123'
    s = ' '
    s = '12 1234 1234 12'
    s = '@##$ $%^&'
    s = '12.0000 1 14.00 2 3 '
    s = 'aaaaaaa'
    s = 'abcabc abc'
    s = '123 a 12 b 13 c'
    s = 'A b a A'
    s = 'CALI cali ABC abc'
    #desc(s)
    
    
    
    