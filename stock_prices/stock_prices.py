#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1]-prices[0]

  for i in range(len(prices)-1):
   current = i
   currentprofit = 0
   for j in range(current+1 ,len(prices[1:]) ):
      # print(f'j: {prices[j]} - current: {prices[current]} = {prices[j]-prices[current]}')
      profit = prices[j] - prices[current]
     
      
      print(profit, currentprofit)
      if profit >= max_profit:
         max_profit = profit
        
  return max_profit

find_max_profit([10, 7, 5, 8, 11, 9])
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))