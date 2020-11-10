'''
Created on Dec 14, 2018

@author: siddardha.teegela
'''
# wc -l filename
# 
# #1. No of lines
# #2. No of characters
# 
# python wc.py -l filename

import sys

def lines(inputFile):
    count  = 0
    with open(inputFile) as iF:
        for line in iF:
            count += 1
    return count

def characters(inputFile):
    count  = 0
    with open(inputFile) as iF:
        for line in iF:
            lineCount = 0
            for char in line:
                lineCount +=1
            count += lineCount
    return count

#def lineAndCharacterCount(inputFile,argument):
    #if argument == "-l":
        

if __name__ == '__main__':
    #sys.argv[0] = wc.py
    #sys.argv[1] = -l
    #sys.argv[2] = filename
    '''
    if sys.argv[1] == "-l":
        lines(fileName)
    elif sys.argv[1] == "-w":
        characters(fileName)
    '''
    
    fileName = "demo.txt"
    print("No of lines:",lines(fileName))
    print("No of chars:",characters(fileName))
    
    
    