'''
Created on Oct 10, 2020

@author: sidteegela
'''

'''
Input: 1->2->3->4->5
Output: 1->5->2->4->3
'''

'''
Approach: 
1. Find the middle of linked list
2. Reverse the second half of linked list
3. merge the 2 sublists
'''


def splitLists(head):
    # Finding the middle node with 2 pointer approach. Slow and fast pointers
    
    while head == None:
        return None

    slow = head
    fast = head
    
    while fast:
        slow = slow.next
        fast = fast.next.next
        
    middle = slow
    
    return head, middle


def reverseList(head):
    
    if head == None:
        return None
    
    prev = head
    current = head
    next = None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = current.next
        
    return prev  # Prev will be the new head


def mergeLists(head_a, head_b):
    
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a
    
    head = tail = head_a
    
    head_a = head_a.next
    while head_b:
        tail.next = head_b
        head_b = head_b.next
        if head_a:
            head_a, head_b = head_b, head_a
            
    return head


def interwearveLists(head):
    if head == None or head.next == None:
        return None
    
    a, b = splitLists(head)
    b = reverseList(b)
    head = mergeLists(a, b)


if __name__ == '__main__':
    pass
