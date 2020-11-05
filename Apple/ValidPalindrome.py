'''
Created on Nov 3, 2020

@author: sidteegela
'''


def isPalindrome(s):

    if s == '':
        return True
    p = 0; q = len(s) - 1
    
    while p < q:
        # print('Initial', s[p], s[q])
        while p < q and not s[p].isalnum():
            p += 1
        while p < q and not s[q].isalnum():
            q -= 1
        # print('Change', s[p], s[q])
        if p < q and s[p].lower() != s[q].lower():
            return False
        
        p += 1; q -= 1
    return True
    
# Time complexity: O(n)
# Space: O(1)

    
if __name__ == '__main__':

    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    
    s = "race a car"
    print(isPalindrome(s))
