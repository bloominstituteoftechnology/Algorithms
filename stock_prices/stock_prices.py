#!/usr/bin/python

import argparse

def find_max_profit(prices):
  highest_price = [0,0]
  lowest_price = [0,0]
  for index, price in enumerate(prices):
    if index == 0:
      lowest_price[0] = price
      lowest_price[1] = index
    if price < lowest_price[0]:
      lowest_price[0] = price
    if price > lowest_price[0] and lowest_price[1] <= highest_price[1]:
      highest_price[0] = price
  print(highest_price, lowest_price)    
     
    
    
  
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))