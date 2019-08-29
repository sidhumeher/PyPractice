'''
Created on Aug 27, 2019

@author: siddardha.teegela
'''

def generateParanteses(n):
    '''
    parens = []
    left = right = n
    
    def generate(p,left,right):
        if left:
            generate(p+'(', left-1, right)
        if right > left:
            generate(p+')', left, right-1)
        if not right:
            parens.append(p)
        return parens
    
    generate('', left, right)
    '''
    
    ret = set()
    memo = set()
    def f(p):
        #print(p)
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