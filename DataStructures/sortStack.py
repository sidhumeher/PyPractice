'''
Created on Jul 14, 2019

@author: siddardha.teegela
'''

from DataStructures.Stack import Stack

def sort_stack(ip):
    result = Stack()
    result.push(ip.pop())
    while ip.size() > 0:
        el = ip.pop()
        count = 0
        print(result.stack)
        while result.peak() > el:
            print('Inside inner while')
            ip.push(result.pop())
            count += 1
        result.push(el)
        
        for item in range(count):
            result.push(ip.pop())
    
    return result

if __name__ == '__main__':
    ip = Stack()
    
    ip.push(1)
    ip.push(3)
    ip.push(4)
    ip.push(2)
    
    result = sort_stack(ip)
    print(result)