'''
Created on Jul 18, 2019

@author: siddardha.teegela
'''

from collections import defaultdict

#Defaultdict works like a dictionary except it does not throw KeyError when you try to
#access a non-existent key

#Assigns a default value to that key with the element of data type passed

if __name__ == '__main__':
    numbers = defaultdict(int)
    
    numbers['one'] = 1
    numbers['two'] = 2
    
    print(numbers['three'])
    
    count = defaultdict(int)
    names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
    for names in names_list:
        count[names] +=1
        
    print(count)
    
    