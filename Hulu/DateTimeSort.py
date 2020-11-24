'''
Created on Nov 23, 2020

@author: sidteegela
'''
from datetime import datetime


def datetimeSort(dates):
    
    def datehelper(date):
        dt = datetime.strptime(date, '%d-%b-%y')
        return dt
        
    dates.sort(key=lambda date:datehelper(date))
        
    print(dates)


def timedelta(dates):
    
    time1 = datetime.strptime(dates[0], '%d-%b-%y')
    time2 = datetime.strptime(dates[1], '%d-%b-%y')
    
    delta = time2 - time1
    print('Days:', delta)
    weeks, days = divmod(delta.days, 7)
    print('Weeks:', weeks)
    print('Days:', days)


if __name__ == '__main__':
    dates = ['05-Nov-18', '25-Mar-17', '01-Nov-18', '07-Mar-17']
    datetimeSort(dates)

    timedelta(dates)
