'''
Created on Aug 23, 2019

@author: siddardha.teegela
'''

from DataStructures.Queue import Queue

def reverseQueue(inputQueue):
    if inputQueue.size() == 0:
        print('Queue is empty')
        return
    
    size = inputQueue.size()
    while size > 0:
        element = inputQueue.dequeue()
        inputQueue.enqueue(element)
        size -= 1
    
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    reverseQueue(q)
    print('After queue reverse')
    q.print()