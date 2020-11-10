'''
Created on Jan 15, 2019

@author: siddardha.teegela
'''


'''
Another example for list comprehension

Lily has a chocolate bar that she wants to share it with Ron for his birthday. 
Each of the squares has an integer on it. She decides to share a contiguous segment 
of the bar selected such that the length of the segment matches Ron's birth month 
and the sum of the integers on the squares is equal to his birth day. You must 
determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares. She wants to find segments 
summing to Ron's birth day d,with a length equalling his birth month m, . 

Output: Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.
'''



def birthday(s, d, m):
    return sum(1 for item in range(len(s)) if sum(s[item:item+m]) == d )

if __name__ == '__main__':
    s = [1,2,1,3,2]
    d = 3
    m = 2
    result = birthday(s, d, m)
    print(result)
