#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # this doesn't work with negative max profit, but does for 3/4 tests

  max_profit_so_far = prices[1] - prices[0]
  current_min_price_so_far = prices[0]

  for price in prices[1:]:
    # current_min_price_so_far = min(current_min_price_so_far, price)
    # max_profit_so_far = max(max_profit_so_far, price - current_min_price_so_far)

    if (price - current_min_price_so_far) > max_profit_so_far:
      max_profit_so_far = price - current_min_price_so_far
    if price < current_min_price_so_far:
      current_min_price_so_far = price
    

  return max_profit_so_far

  # Didn't work:
  # purchase = 0
  # sell = 0
  # max_profit_so_far = -1
  # change_index = True

  # for i in range(0, len(prices) - 1):
  #   sell = prices[i + 1]

  #   if change_index:
  #     purchase = prices[i]

  #   elif sell < purchase:
  #     change_index = True
  #     continue

  #   else:
  #     temporary_profit = sell - purchase
  #     if temporary_profit > max_profit_so_far:
  #       max_profit_so_far = temporary_profit
  #     change_index = False

  # return max_profit_so_far

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))