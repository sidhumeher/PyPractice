'''
Created on Oct 20, 2020

@author: sidteegela
'''
import re


def mostCommonWord(paragraph, bannedList):
    
    if len(paragraph) == 0:
        return None
    
    # Substitute special chars
    paragraph = re.sub('\W +', ' ', paragraph)
    
    # Convert to lower case and split words
    wordList = paragraph.lower().split(' ')
    
    # Store them in dictionary
    wordDictionary = {}
        
    for word in wordList:
        if word not in bannedList:
            if word not in wordDictionary:
                wordDictionary[word] = 1
            else:
                wordDictionary[word] += 1
     
    mostFrequentWord = ''
    mostFrequentTime = 0      
    # print(wordDictionary)
    
    for key, value in wordDictionary.items():
        if value > mostFrequentTime:
            mostFrequentTime = value
            mostFrequentWord = key
    
    print(mostFrequentWord)
    print(f'{mostFrequentWord} appeared {mostFrequentTime} times')
    
# Time Complexity: O(n + m), n = No of words in input and m= no of words in banned list
# Space: O(n + m), n = size of wordList and m = size of Dictionary
    
    
if __name__ == '__main__':
    paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
    bannedList = ["hit"]
    
    mostCommonWord(paragraph, bannedList)
