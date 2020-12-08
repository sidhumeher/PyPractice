'''
Created on Dec 7, 2020

@author: sidteegela
'''

# Given a number find nearest palindrome


def isPalindrome(num):
    
    numToStr = str(num)
    p = 0; q = len(numToStr) - 1
    
    while p <= q:
        if numToStr[p] != numToStr[q]:
            return False
        p += 1; q -= 1
        
    return True


# Smallest and largest palindrome to the given input
def findPalindrome(num):
    
    if 0 <= num <= 9:
        return num
    
    smallestPalindrome = num
    while isPalindrome(smallestPalindrome) != True:
        smallestPalindrome -= 1
        
    print('SmallestPalindrome:', smallestPalindrome)
    
    largestPalindrome = num
    while isPalindrome(largestPalindrome) != True:
        largestPalindrome += 1
        
    print('LargestPalindrome:', largestPalindrome)


if __name__ == '__main__':
    num = 1233
    findPalindrome(num)
    
