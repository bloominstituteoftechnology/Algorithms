#!/usr/bin/python

import argparse

'''
finding max profits by buying first and selling later
takes in a list of numbers representing prices
the max profit is going to be max_price - low_price

if I step through the array keeping track of the lowest price I find
and subtracting it from the max price then keep track of which max prices
are the largest I should get the max profit possible

buy_price = low_price
sell_price = max_price

ok so my inital solution works for the first test set
but not for the second set where there's no way to make a profit
I don't think my solution really takes into account the fact that 
you have to buy before you sell

so if I walk through the list when I find a lower buy price and then if that 
is able to find a higher profit then set those values

'''


def find_max_profit(prices):
  low_price = max_price = prices[0]

  for p in prices:

    if p < low_price:
      low_price = p

    if max_price - low_price < p - low_price:
      max_price = p
    #if sell_price - p > sell_price - buy_price:

  return max_price - low_price 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))