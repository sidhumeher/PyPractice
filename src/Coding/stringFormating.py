'''
Created on Feb 15, 2019

@author: siddardha.teegela
'''

def print_full_name(a, b):
    print("Hello {} {}! You just delved into Python3".format(a,b))
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)