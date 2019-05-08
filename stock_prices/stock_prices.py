#!/usr/bin/python

import argparse

def find_max_profit(prices):
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
a = [100, 90, 80, 50, 20, 10]
print(find_max_profit(a))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))