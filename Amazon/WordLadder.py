'''
Created on Nov 30, 2020

@author: sidteegela
'''
from _collections import defaultdict, deque


def ladderLength(beginWord, endWord, wordList):
    
    if endWord not in wordList:
        return 0
    
    # combinations of words
    all_combo = defaultdict(list)
    
    for word in wordList:
        for i in range(len(beginWord)):
            all_combo[word[:i] + '*' + word[i + 1:]].append(word)
            
    # print(all_combo)
    
    # queue for BFS
    q = deque([(beginWord, 1)])
    # To keep track of visited nodes
    visited = {beginWord:True}
     
    while q:
        current_word, level = q.popleft()
        for i in range(len(beginWord)):
            intermediate_word = current_word[:i] + '*' + current_word[i + 1:]
            
            # find next states of current word
            for word in all_combo[intermediate_word]:
                if word == endWord:
                    return level + 1
                # add to queue. Also mark as visited
                if word not in visited:
                    visited[word] = True
                    q.append((word, level + 1))
            all_combo[intermediate_word] = []
            
    return 0

# Time complexity: O(m^2,n), m=length of each word,n=no of words in word list
# Space: O(m^2,n)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(ladderLength(beginWord, endWord, wordList))
