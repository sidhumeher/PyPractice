'''
Created on May 5, 2020

@author: sidteegela
'''

def isPalindrome(s):
    
    #Ignoring cases
    s = s.lower()
    
    #Removing characters that are not alphabet and numbers
    stripped_s = ''
    
    for item in s:
        if item.isdigit() or item.isalpha():
            stripped_s += item
            
    if stripped_s == stripped_s[::-1]:
        return True
    else:
        return False
    
# Run time: 44ms
# Memory 14.2 MB

if __name__ == '__main__':
    
    s= 'A man, a plan, a canal: Panama'
    print(isPalindrome(s))
    
    s= 'race a car'
    print(isPalindrome(s))