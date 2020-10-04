'''
Created on Mar 29, 2020

@author: sidteegela
'''

def maxProfit(prices):
    
    max_profit = 0 
    
    for i in range(len(prices)-1):
        max_profit += max(prices[i+1]-prices[i],0)
    
    return max_profit

    '''
    if len(prices) == 0:
        return 0
    elif len(prices) == 2 and prices[1]-prices[0] > 0:
            return prices[1]-prices[0]
    elif len(prices) == 2 and prices[1]-prices[0] < 0:
            return 0
    
    final_profit = 0
    total_profit = 0
    day_of_buy = 0
    day_of_sell = 1
    
    while day_of_buy < len(prices) and day_of_sell < len(prices):
        
        current_profit = prices[day_of_sell] - prices[day_of_buy]
        if current_profit <= 0:
            day_of_buy += 1
            day_of_sell += 1
        if current_profit > 0:
            total_profit += current_profit
            day_of_buy += 2
            day_of_sell += 2 
        
        final_profit = max(final_profit,total_profit)
    '''

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    
    finalProfilt = maxProfit(prices)
    print(finalProfilt)
    
    prices = [1,2,3,4,5]
    finalProfilt = maxProfit(prices)
    print(finalProfilt)