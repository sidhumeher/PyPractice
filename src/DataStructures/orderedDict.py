'''
Created on Jul 18, 2019

@author: siddardha.teegela
'''

from collections import OrderedDict
from collections import Counter

#Maintains the order in which keys are inserted

if __name__ == '__main__':
    oc = OrderedDict()
    oc['a'] = 1
    oc['b'] = 2
    oc['c'] = 3
    
    #print(oc)
    
    #for key,value in oc.items():
    #    print(key,value)
        
    
    #Most frequently occurring element will be placed first
    list = ["a","c","c","a","b","a","a","b","c"]
    cntr = Counter(list)
    #print(cntr.most_common())
    
    oc = OrderedDict(cntr.most_common())
    for key,value in oc.items():
        print(key,value)
    
    