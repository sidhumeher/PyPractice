'''
Created on Jul 18, 2019

@author: siddardha.teegela
'''

from collections import ChainMap

#Used to combine several dictionaries/mappings. Returns a list of mappings

if __name__ == '__main__':
    dict1 = {'a':1,'b':1,'c':1}
    dict2 = {'a':2,'b':2,'c':2}
    
    cm = ChainMap(dict1,dict2)
    print(cm)
    print(cm.maps)
    
    #Accessing a key in list of dictionaries
    print(cm['a'])
    
    #Updating a dictionary will update the Chainmap as well
    dict2['a'] = 3
    print(cm.maps)
    
    #Accessing keys and values of chainmap
    #When one key appears in more than one dictionary, chainmap will take value from first dictionary
    print(list(cm.keys()))
    print(list(cm.values()))
    
    #Adding new dictionary to chainmap
    dict3 = {'e':1,'f':1}
    cm = cm.new_child(dict3)
    print(cm)
    
    print(list(cm.keys()))
    print(list(cm.values()))
    
    
    
    