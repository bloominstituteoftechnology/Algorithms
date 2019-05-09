#!/usr/bin/python

from random import randint
import time
import argparse
import math


start = (time.time())

def find_max_profit(prices):
 min = prices[0]
 max = prices[0]
 for i in range(0, len(prices)-1):
   if min > prices[i]:
     min = prices[i]
     max = prices[i + 1]
   elif max < prices[i]:
     max = prices[i]
 return max - min

print(find_max_profit([1050, 270, 1540, 3800, 2]))

end_time = (time.time())

ivan_total_time = end_time - start

start = time.time()



def find_max_profit1(prices):
  min_price = prices[0]
  max_profit = prices[1] - min_price

  for i in range(1, len(prices)):
    price = prices[i]
    max_profit = max(price - min_price, max_profit)
    min_price = min(price, min_price)

  return max_profit

find_max_profit([1050, 270, 1540, 3800, 2])

end_time = time.time()

lambda_total_time = end_time - start

start = time.time()

def find_max_profit2(prices):
  max_profit = -10
  buy_price = 0
  sell_price = 0
  
  # this allows our loop to keep iterating the buying
  # price until a cheap stock price is found
  change_buy_index = True
  
  # loop through list of stock prices once
  for i in range(0, len(prices)-1):
    
    # selling price is the next element in list
    sell_price = prices[i+1]
    
    # if we have not found a suitable cheap buying price yet
    # we set the buying price equal to the current element
    if change_buy_index: 
      buy_price = prices[i]
    
    # if the selling price is less than the buying price
    # we know we cannot make a profit so we continue to the 
    # next element in the list which will be the new buying price
    if sell_price < buy_price:
      change_buy_index = True 
      continue
    
    # if the selling price is greater than the buying price
    # we check to see if these two indices give us a better 
    # profit then what we currently have
    else:
      temp_profit = sell_price - buy_price
      if temp_profit > max_profit:
        max_profit = temp_profit
      
      change_buy_index = False
      
  return max_profit

find_max_profit([1050, 270, 1540, 3800, 2])

end_time = time.time()

sergey_total_time = end_time - start

start = time.time()

def find_max_profit3(prices):

  if len(prices) > 1:
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]

  for n in prices[1:]:
    if n < current_min_price_so_far:
      current_min_price_so_far = n
      continue
    elif (n - current_min_price_so_far) > max_profit_so_far:
      max_profit_so_far = n - current_min_price_so_far
  
  return max_profit_so_far

find_max_profit([1050, 270, 1540, 3800, 2])

end_time = time.time()

ben_total_time = end_time - start


start = time.time()

def find_max_profit4(prices):
  
  profit = prices[1] - prices[0]

  for i in range(len(prices)-1):
    for j in range(i+1, len(prices)-1):
      if prices[j] - prices[i] > profit:
        profit = prices[j] - prices[i]

  return profit

find_max_profit([1050, 270, 1540, 3800, 2])

end_time = time.time()

jonah_total_time = end_time - start

print('Ivan total time', ivan_total_time)
print('lambda_total_time total time', lambda_total_time)
print('sergey_total_time total time', sergey_total_time)
print('ben_total_time total time', ben_total_time)
print('jonah_total_time total time', jonah_total_time)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))