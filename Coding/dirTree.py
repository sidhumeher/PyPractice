'''
Created on Oct 17, 2018

@author: siddardha.teegela
'''
import os;

def print_dir_contents(path):
    for contents in os.listdir(path):
        subContent = os.path.join(path,contents)
        if os.path.isdir(subContent):
            print_dir_contents(subContent)
        else:
            print(subContent) 
        
        

if __name__ == '__main__':
    #pass
    print_dir_contents('C:\\Users\\siddardha.teegela\\Downloads\\New hire packet 2')