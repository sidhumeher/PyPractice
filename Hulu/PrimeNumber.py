'''
Created on Nov 20, 2020

@author: sidteegela
'''
import math

# A prime is greater than 1 and only divisible by 1 and itself. No other factors


# checks if a number is prime
def isPrime(num):
    
    if num <= 1:
        print('Not prime')
        return
        
    for i in range(2, num):  # we can also use range(2,num//2)
        if num % i == 0:
            print('Not prime')
            return

    print('Input is prime')

'''
We can check till root of num because a larger factor of num must be multiple of 
smaller factor of num that has already been checked
'''    


def isPrimeOptimized1(num):
    
    if num <= 1:
        print('Not prime')
        return
    
    upperbound = math.floor(math.sqrt(num))
    
    for i in range(2, upperbound + 1):
        if num % i == 0:
            print('Not prime')
            return
    print('Prime number')    

'''
In the above method we iterated through all even numbers, it is a waste
All even numbers except 2 are divisible by 2 and so cannot be Prime nos.
We will eliminate all even nos. and only check odd nos.
'''


def isPrimeOptimized2(num):
    
    if num <= 1:
        print('Not prime')
        return 
    if num == 2:
        print('Prime number')
        return 
    if num > 2 and num % 2 == 0:  # Eliminating all even numbers
        print('Not prime')
        return
    
    upperbound = math.floor(math.sqrt(num))
    
    for i in range(3, upperbound + 1, 2):
        if num % i == 0:
            print('Not a Prime')
            return
    print('Prime Number')

'''
All primes can be represented in the from 6k +/- i with exception of 2 and 3
Because all integers can be expressed as 6k+1 for some integer k and i = 1,2,3,4
2 divides 6k+0, 6k+2, 6k+4
3 divides 6k+3
'''


def isPrimeOptimized3(num):
    
    # Corner cases
    if num <= 1:
        print('Not a prime')
        return 
    if num <= 3:
        print('Prime number')
        return

    if num % 2 == 0 or num % 3 == 0:
        print('Not a prime')
        return
    
    i = 5
    while i * i <= num:
        print('i Before:', i)
        if num % i == 0 or num % (i + 2) == 0:
            print('Not a prime')
            return
        i += 6
        print('i After:', i)
        
    print('Prime number')

    
# Print primes within a range
def primeNumbersinRange(num):
    
    if num <= 1:
        return 
    
    for item in range(num + 1):
        if item > 1:
            for divide in range(2, item // 2):
                if item % divide == 0:
                    break
            else:
                print(item)
        
    return 


if __name__ == '__main__':
    num = 407
    # isPrime(num)
    
    num = 7
    # isPrime(num)
    
    # Prime numbers range
    # primeNumbersinRange(15)
    
    # Optimized solution
    isPrimeOptimized1(97)
    isPrimeOptimized2(97)
    isPrimeOptimized3(97)
