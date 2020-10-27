'''
Created on Oct 21, 2020

@author: sidteegela
'''


# Finding Substring or pattern matching of a string with Rabin Karp algorithm
# Time complexity: Avg case: O(n+m). Worst case: o(n*m) for a bad hash function
def search(pattern, text, q):

    d = len(text)  # Taken as length of text. But can be any number
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    
    for _ in range(m - 1):
        h = (h * d) % q
    print(h)
    
    # Calculate hash of pattern and text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q  # ord() takes unicode char and returns integer representation
        t = (d * t + ord(text[i])) % q
        
    # Find match
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1  # If you get here it means we found a match and j=2,increment it to match pattern length
            
            if j == m:
                print('Pattern found at index:', i)
                
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            
            if t < 0:
                t = t + q


def subString(s1, s2):
    
    # using 'in'
    '''
    if s1 != None and s2 != None:
        if s2 in s1:
            print(True)
        else:
            print(False)
    '''
    
    # Using find(). Returns -1 if not found
    if s1.find(s2) != -1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    
    text = 'ABCCDDAEFG'
    pattern = 'CDD'
    q = 13  # Random prime number
    
    # Using Rabin Karp algorithm
    search(pattern, text, q)
    
    # Using builtin functions
    subString('ABCCDDAEFG', 'CDD')
