'''
Created on Apr 9, 2019

@author: siddardha.teegela
'''

'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s == '12:00:00 AM':
        return '00:00:00'
    elif s == '12:00:00 PM':
        return '12:00:00'
    
    splitStr = s.split(':')
    if 'PM' in splitStr[2]:
        if splitStr[0] == '12':
            return splitStr[0]+':'+splitStr[1]+':'+splitStr[2].replace('PM','')
        else:
            return str(int(splitStr[0])+12)+':'+splitStr[1]+':'+splitStr[2].replace('PM','')
    else:
        return splitStr[0]+':'+splitStr[1]+':'+splitStr[2].replace('AM','')
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
