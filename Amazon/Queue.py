'''
Created on Oct 19, 2020

@author: sidteegela
'''
'''
Queue in Python can be implemented in 3 ways
1. Lists - Inserting or deleting an item is slow as it requires shifting items
2. collection.deque - Enqueue and dequeue are faster. O(1) time
3. queue.Queue

'''

from collections import deque
from queue import Queue

if __name__ == '__main__':
    
    # Dequeue
    d = deque()
    
    # Adding items to queue
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.append(5)
    
    print(d)
    
    # Remove items for queue
    print(d.popleft())  # Removes the item from left. First inserted item
    print(d)
    
    # pop() will remove the item from the right. Last insetred item
    
    # queue implementation from Queue class
    q1 = Queue(maxsize=5)
    
    print(q1.empty())  # True if queue is empty,otherwise False
    
    q1.put(1)
    q1.put(2)
    q1.put(3)
    
    print(q1.get())  # Removes and returns the first inserted item
    
    '''
    Queue also has put(item, block, timeout) which waits until a space is available
    and get(block, timeout) which waits until an item is available to remove
    Alternative. put_nowait() and get_nowait()
    '''
