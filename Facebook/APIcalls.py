'''
Created on Oct 18, 2020

@author: sidteegela
'''

import os
import socket
import requests


def makeRequest():
    
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    location = 'Rose garden'

    PARAMS = {'address':location}

    r = requests.get(url=URL, params=PARAMS)

    returnData = r.json()

    print(returnData)


def checkPingWithSocket():
    
    ip = 'google.com'
    port = 443
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    
    try:
        s.connect(ip, port)
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()
        
        
def checkPingWithOS():
    
    host = 'google.com'
    
    response = os.system("ping -c 1 " + host)
    
    if response == 0:
        print(host + ' is reachable')
    else:
        print(host + ' is unreachable')
    
    # print(response)

        
if __name__ == '__main__':
    
    print(checkPingWithSocket())
    
    if checkPingWithSocket():
        print('Site is up')
    else:
        print('Site is down')
    
    print('\n')
    checkPingWithOS()
