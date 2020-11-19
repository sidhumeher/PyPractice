'''
Created on Nov 16, 2020

@author: sidteegela
'''


def reorderLogFiles(logs):
    
    if len(logs) == 0:
        return 
    
    letterLogs = []; digitLogs = []

    # Custom key method to sort lexicographically
    def order(log):
        splitList = log.split(' ')
        key, rest = splitList[0], splitList[1:]
        # return ' '.join(rest) + ' ' + key
        return splitList[1]

    for log in logs:
        logsplit = log.split(' ')
        if logsplit[1].isalpha():
            letterLogs.append(log)
        else:
            digitLogs.append(log)

    letterLogs.sort(key=order)
    return letterLogs + digitLogs


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorderLogFiles(logs))

    # Example output ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
