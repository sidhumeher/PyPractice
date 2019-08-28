'''
Created on May 5, 2019

@author: siddardha.teegela
'''

def nonDivisibleSubset(k, s):
    result = 0
    reminder_list = []
    
    '''Reminders of all items in s % k'''
    for i in s:
        reminder_list.append(i % k)
        
    ''' If a numeber is evenly divider by k then adding any other number to it 
    does not divide it evenly by k. Add it to result''' 
    if 0 in reminder_list:
        result += 1
        
    ''' Removing 0 reminders '''
    reminder_list = [x for x in reminder_list if x != 0]
    counter = [0] * k
    
    for i in range(len(reminder_list)):
        ''' Occurance of each reminder with itself as index'''
        counter[reminder_list[i]] += 1
        
    index = []
    
    for i in range(len(counter)):
        maxCount = max(counter)
        maxIndex = counter.index(maxCount)
        
        if k - maxIndex not in index and maxCount != 0:
            index.append(maxIndex)
        if maxIndex * 2 % k  == 0:
            result += 1
        else:
            result = maxCount
        counter[maxIndex] = 0
        
    print(result)
        
    
   
if __name__ == '__main__':
    k = 3
    s = [1,7,2,4]
    result = nonDivisibleSubset(k, s)
   