#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # each value in prices represents a price on a given day. Once a stock is bought, it can only be sold at a price found to the right of it in the prices list
  # loop through prices
  # the value of the current index is represented as the buy price
  # the value of all indexes after the current index is represented as the sell price
  # at each interval of the loop, the buy price should be subtracted from the sell price
  # the result of sell price - buy price is stored as max profit
  # at each interval of the loop, if the result of the current inverval's sell price - buy price is a higher value than what's currently stored in max profit, then overwrite max profit's current value with new result
  # return max profit
  buy_price = 0
  sell_price = 0
  max_profit = 0

  for i in range(0, len(prices)):
    cur_index = i
    buy_price = prices[i]

    for x in range(cur_index, len(prices)):
      sell_price = prices[x]
      if max_profit < sell_price - buy_price:
        max_profit = sell_price - buy_price

  # if max_profit's value is still zero or less after looping through the list, that means taking a loss on the buy_price's value is the optimal value
  if max_profit <= 0:
    max_profit = buy_price * -1

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))