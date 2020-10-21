'''
Created on Oct 19, 2020

@author: sidteegela
'''
'''
Given sides of triangle, find out of it is Right angled, Acute angle, Obtuse angle

Right angled triangle: c^2 = a^2 + b^2
Acute angled triangle: c^2 < a^2 + b^2
Obtuse angled triangle: c^2 > a^2 + b^2
'''


def checkTraingle(a, b, c):
    
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)
    
    if a == (b + c) or b == (a + c) or c == (a + b):
        print('Right angled triangle')
        return 
    if a < (b + c) or b < (a + c) or c < (a + b):
        print('Acute angled triangle')
        return 
    else:
        print('Obtuse angled triangle')
        return
    

if __name__ == '__main__':
    checkTraingle(1, 2, 3)
    checkTraingle(4, 2, 2)
