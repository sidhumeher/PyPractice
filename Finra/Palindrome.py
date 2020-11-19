'''
Created on Nov 17, 2020

@author: sidteegela
'''
# Check if a string is a Palindrome


# Two pointer approach
def isPalindrome(s):
    
    # Ignoring cases
    s = s.lower()
    
    left = 0; right = len(s) - 1
    
    while left != right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left] != s[right]:
                return False
            else:
                left += 1; right -= 1
        elif not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        
    return True


# Reverse string approach
def isPalindrome1(s):
    
    if s == '':
        return True
    
    if s == s[::-1]:
        return True
    
    return False

    
if __name__ == '__main__':
    s = 'No lemon, no melon'
    print(isPalindrome(s))
    
    s = 'radar'
    # print(isPalindrome(s))
    print(isPalindrome1(s))
    
    s = 'Geeks and geeks'
    # print(isPalindrome(s))
    print(isPalindrome1(s))
