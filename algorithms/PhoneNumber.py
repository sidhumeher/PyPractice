'''
Created on Aug 26, 2019

@author: siddardha.teegela
'''

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.A mapping of digit to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.
'''

# EXAMPLE OF RECURSSION

def generateCombinations(reference, ip):
    op = []
    
    def recurssion(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            op.append(combination)
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in reference[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                recurssion(combination+letter, next_digits[1:])
                
    if ip:
        recurssion('',ip)
    
    return op
    

if __name__ == '__main__':
    digits_to_letters = dict()
    
    digits_to_letters.update({'2':['a','b','c']})
    digits_to_letters.update({'3':['d','e','f']})
    digits_to_letters.update({'4':['g','h','i']})
    digits_to_letters.update({'5':['j','k','l']})
    digits_to_letters.update({'6':['m','n','o']})
    digits_to_letters.update({'7':['p','q','r','s']})
    digits_to_letters.update({'8':['t','u','v']})
    digits_to_letters.update({'9':['w','x','y','z']})
    
    ip = '23'
    output = generateCombinations(digits_to_letters, ip)
    print(output)
    
    ip = '234'
    output = generateCombinations(digits_to_letters, ip)
    print(output)