'''
Created on Jul 16, 2019

@author: siddardha.teegela
'''
import collections

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    def get(self,key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1
    
    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False) #Return and remove the key,value pair in FIFO
        self.cache[key] = value