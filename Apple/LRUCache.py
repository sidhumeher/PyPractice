'''
Created on Nov 5, 2020

@author: sidteegela
'''
# LRU cache implementation with Ordered Directory Python

# Ordered Dict performs get,put,delete key in O(1) time. It combines behind a hashmap and linkedlist

from collections import OrderedDict


class LRUCache(OrderedDict):
    
    def __init__(self, capacity):
        self.capacity = capacity
        
    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last=False)

# Time complexity: O(1) for get and put
# get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done in a constant time.
# Space: O(capacity)


if __name__ == '__main__':
    lruObj = LRUCache(2)
    print(lruObj.get(1))
    lruObj.put(1, 1)
    
    print(lruObj)
