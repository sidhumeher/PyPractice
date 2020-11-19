'''
Created on Nov 17, 2020

@author: sidteegela
'''
import re


def search(s):
    
    if len(s) == 0:
        return None
    
    result = re.findall('^demo', 'this is a demo program')
    return result


if __name__ == '__main__':
    s = 'this is a demo program'

    for word in list(s.split(' ')):
        if word.startswith('d') and word.endswith('o'):
            print(word)

    s = 'this is a demo program'
    print(search(s))
