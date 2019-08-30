'''
Created on Aug 27, 2019

@author: siddardha.teegela
'''

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def generateParanteses(n):
    
    ret = set()
    memo = set()
    def f(p):
        #print(p)
        print(memo)
        if p in memo:
            return
        memo.add(p)
        if len(p) == 2 * n:
            ret.add(p)
            return
        for i in range(len(p)):
            print(i,p[:i])
            print(i,p[i:])
            #print(p[:i] + '()' + p[i:])
            f(p[:i] + '()' + p[i:])

    f('()')
    return ret

if __name__ == '__main__':
    n = 3 
    result = generateParanteses(n)
    print(result)