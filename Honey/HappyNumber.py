'''
Created on Nov 13, 2020

@author: sidteegela
'''


def happyNumber(num):
    
    def getNext(n):
        sum = 0
        while n > 0:
            n, reminder = divmod(n, 10)
            sum += reminder ** 2
        return sum
    
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = getNext(num)
        
    return num == 1

# Time complexity: O(logn)
# Space: O(logn n)


if __name__ == '__main__':
    num = 123
    print(happyNumber(num))
    
    num = 19
    # print(happyNumber(num))
