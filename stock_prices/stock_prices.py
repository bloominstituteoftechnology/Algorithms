#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # initiate max_profit to difference between first set of prices.  Use it as benchmark for future comparison
  max_profit = prices[1] - prices[0]
  # iterate through prices list to define each buy price
  for buy_price_index, buy_price in enumerate(prices):
    # If buy_prices reaches the last element, end loop since no more sell price to compare with
    if buy_price_index == len(prices) - 1:
      break
    # find the highest sell price subsequent to the buy price
    max_sell_price = max(prices[buy_price_index+1:])
    # define the max profit generated from max sell price and current buy price
    current_max_profit = max_sell_price - buy_price
    # if current max profit is greater than the max profit to date, assign current max profit to current max profit
    if current_max_profit > max_profit:
      max_profit = current_max_profit
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))