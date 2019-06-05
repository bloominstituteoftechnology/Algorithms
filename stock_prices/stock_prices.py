#!/usr/bin/python

import argparse

# "prices" is an array/list of a day's stock price variation (positive ints)
# function should return "max_profit" from buy & sell that day
# must buy before selling
# "max_profit" can be negative int
def find_max_profit(prices):
    # to keep track of highest profits:
    max_profit = None
    for i in range (0, len(prices)):
        # substracting each price to each one ahead
        # and keeping only if greater than "max_profit"
        for j in range(i+1, len(prices)):
            #profit -> prices[j]-prices[i] == sell_price-buy_price
            profit = (prices[j]-prices[i])
            # make "max_profit" = to "profit" in first iteration
            # or when "profit" is greater than "max_profit"
            if i == 0 or profit > max_profit:
                max_profit = profit
    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))