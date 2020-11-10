'''
Created on Jan 7, 2019

@author: siddardha.teegela
'''
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    charCount = Counter(s1)
    charCount.subtract(s2)
    
    result = 0 
    for x in charCount.values():
        result += abs(x)
    return result
    
    
if __name__ == '__main__':
    s1 = 'abc'
    s2 = 'amnop'
    result = makingAnagrams(s1, s2)
    print(result)
    
    s1 = 'cde'
    s2 = 'abc'
    result = makingAnagrams(s1, s2)
    print(result)
    
    s1 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
    s2 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
    result = makingAnagrams(s1, s2)
    print(result)