'''
Created on Aug 27, 2019

@author: siddardha.teegela
'''

def generateParantneses(n):
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

if __name__ == '__main__':
    n = 3 
    result = generateParantneses(n)
    print(result)