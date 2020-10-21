'''
Created on Oct 18, 2020

@author: sidteegela
'''
from collections import OrderedDict
from collections import defaultdict

import csv

# Hash map/Dictionary
'''
Hash tables/maps in Python are implemeneted with Dictionary data type
Keys are generated with Hash function. Elements are not ordered and unsorted and can be changed

Creation: using dict() or {}
'''


def test_dict():
    
    myDict = {'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
    
    # Accessing keys and values
    print('Accessing keys and values:')
    print(myDict.keys())
    print(myDict.values())

    print(myDict['Dave'])
    print('\n')
    
    # Sorting a Dictionary
    # sorted()- Sorts items by key
    
    print('Dictionary sorting:')
    newSortedDict = sorted(myDict)
    print(newSortedDict)
    
    print('\n')
    
    # For loop
    print('Accessing items with for loop')
    for item in myDict:  # Only keys
        print(item)
    for item in myDict.values():  # Only values
        print(item)
    for key, value in myDict.items():  # Both key and value
        print(key, value)
    
    # Delete item from Dictionary
    '''
    del myDict['Dave']
    myDict.pop('Dave')
    myDict.popitem()  # Removes last inserted item
    myDict.clear() # Clears all items in dictionary
    '''


def dictinarySorting():

    orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
    }
    
    # Sort by value
    print('\n')
    print('Sorting by value-Descending order')
    sorted_orders = sorted(orders.items(), key=lambda x:x[1], reverse=True)
    print(sorted_orders)
    
    print('\n')
    print('Sorting by value-Ascending order')
    sorted_orders = sorted(orders.items(), key=lambda x:x[1])
    print(sorted_orders)

# Dictionary types


def orderedDictionary():
    
    myDict = OrderedDict()

    myDict['Dave'] = 1
    myDict['Ava'] = 2
    myDict['Joe'] = 3
    
    # Maintains insertion order
    # If value of a key changes, the position remains unchanged
    # Deleting and reinserting a key pushed it to back of the order
    print('\nOrdered Dictionary')
    print(myDict)

    # Popitem() return and removes key-value. LIFO order if last=True, FIFO order if last=False
    
    print(myDict.popitem(last=True))
    myDict['Joe'] = 3
    print(myDict.popitem(last=False))
    myDict['Mermaid'] = 9
    print(myDict)

    '''
    move_to_end() moves a key to first or last of dictionary.
    last=True, moves to last
    last=False moves to first
    '''
    
    myDict.move_to_end('Mermaid', last=False)
    print(myDict)
    myDict.move_to_end('Ava', last=True)
    print(myDict)

    
def defaultDir():
    print('\nDefault Dictionary')
    myDict = defaultdict(list)  # Default value is an empty list
    mylist = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]

    for k, v in mylist:
        myDict[k].append(v)

    print(myDict)

# File reading and writing operations


def fileOperations():
    
    print('\nFile Reading')
    fileReader = open('demofile')  # Returns a file object. By default returns TextIOWrapper object
    
    try:
        fileReader.read()  # Reads entire file
        print(fileReader.readline(9))
        # print(fileReader.readline(10)) #Reads only given no of chars per line
        # fileReader.readlines() #Returns lines as a list
        
    except:
        pass
    
    finally:
        fileReader.close()
    
    '''
    Another way to file open and close is as follows.
    with open(demofile, 'r') as fileReader:
        fileReader.readline()
        
    File modes:
    r - read only
    w - write,truncating
    rb/wb - read/write binary mode
    '''
        
    print('\nFile Writing')
    
    with open('demofile', 'w') as reader:
        reader.write('This is a demo write operation')
        reader.writelines('\nThis is demo write line')

    # Path name of the file (__file__)
    print(__file__)
    
    '''
    Appending to a file
    Use 'a' mode
    '''
    with open('demofile', 'a') as fileReader:
        fileReader.write('\nThis is demo line to append to line')


def readCVS():
    
    with open('demoCSV') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        
        for line in csvreader:
            print(line)


if __name__ == '__main__':
    
    # Map/Dictionary usage in Python
    test_dict()
    dictinarySorting()
    orderedDictionary()
    defaultDir()
    
    # File reading and writing operations
    fileOperations()

    # Standard input and output operations
    print('Standard input operations\n')
    print('Enter a name:')
    name = str(input())
    print('Entered name:', name)
    
    # CSV file reader
    print('\n')
    readCVS()
