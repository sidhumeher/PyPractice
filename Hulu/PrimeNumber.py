'''
Created on Nov 20, 2020

@author: sidteegela
'''

# A prime is greater than 1 and only divisible by 1 and itself. No other factors


def isPrime(num):
    
    if num <= 1:
        print('Not prime')
        return
        
    for i in range(2, num - 1):  # we can also use range(2,num//2)
        if num % i == 0:
            print('Not prime')
            return

    print('Input is prime')


if __name__ == '__main__':
    num = 407
    isPrime(num)
    
    num = 7
    isPrime(num)
