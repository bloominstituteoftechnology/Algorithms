#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy = 0
  buy_index = 0
  sell = 0
  profit = 0
  
  for i in prices:
    if buy==0 or i<buy and i!= prices[-1]:
      buy = i 
      buy_index = prices.index(i) 
      print('buy is {buy}'.format(buy=buy))
    if i==0 or i>sell and prices.index(i) > buy_index or sell==0 and i==prices[-1]:
      sell = i
      print('sell is {sell}'.format(sell=sell))
      profit = sell -buy
   
    
  print('The stock was bought at ${buy} and sold at ${sell} for a profit of ${profit}'.format(buy=buy, sell=sell, profit=profit))
  return(profit)
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))