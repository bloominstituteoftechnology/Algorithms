#!/usr/bin/python

import argparse

def find_max_profit(prices):
  update_buy=True
  buy_price=0
  profit=0
  count_negative=1
  for i in range (len(prices)-1):
    sell_price=prices[i+1]
    if update_buy:
      buy_price= prices[i]
    if sell_price<buy_price:
      update_buy=True
      count_negative+=1
    else:
      update_buy=False
      temp_profit= sell_price-buy_price
      if temp_profit> profit:
        profit=temp_profit
  if count_negative==len(prices):
    return prices[len(prices)-1]- prices[len(prices)-2]
  else:
    return profit
      
      
    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))