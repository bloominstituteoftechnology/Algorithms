#!/usr/bin/python

import argparse

def find_max_profit(prices):

  largest_index = 0
  smallest_index = 0
  j = 0
  
  for i, price in enumerate(prices):
    price = prices[i]
    #print(price)
    
    if price > prices[largest_index]:
      
      largest_index = i



  while j < largest_index:
    
    #print(j)
    if prices[j] < prices[smallest_index]:
      #print(prices[j])
      smallest_index = j
    j += 1
    #print(smallest_index)

  print(prices[largest_index] - prices[smallest_index])

  return prices[largest_index] - prices[smallest_index]

  
find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))