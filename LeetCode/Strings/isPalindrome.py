'''
Created on May 5, 2020

@author: sidteegela
'''


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


if __name__ == '__main__':
    
    s = 'A man, a plan, a canal: Panama'
    print(isPalindrome(s))
    
    s = 'race a car'
    print(isPalindrome(s))
    
    s = 'No lemon, no melon'
    print(isPalindrome(s))
    
    s = 'Was it a cat I saw?'
    print(isPalindrome(s))
