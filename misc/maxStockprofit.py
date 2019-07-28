'''
Function should return the maximum profit you can make from a 
single buy and sell, given an array of prices

Find minBuy first before looking for maxSell
'''
import math
def find_max_profit(prices):
    # find minBuy before maxSell
    minBuy = prices[0]
    maxSell = 0
    for i in prices[1:]:
        if maxSell == 0 and minBuy > i:
            minBuy = i
        else:
            maxSell = max(maxSell,i)
    
    return(f'Sell {maxSell} - buy {minBuy} = {maxSell - minBuy}')
        
        


print(find_max_profit([10, 7, 5, 8, 11, 9]));       # should print 6
print(find_max_profit([1050, 270, 1540, 3800, 2]))  # should print 3530
print(find_max_profit([100, 90, 80, 50, 20, 10]));  # should print -10
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]));   # should print 94