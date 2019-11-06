#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_price = prices[1]
  min_price = prices[0]
  max_profit = max_price - min_price

  for i in range (len(prices)):
    for j in range(i + 1, len(prices)):


      if prices[j] - prices[i] > max_profit:
        max_price = prices[j]
        min_price = prices[i]
        max_profit = max_price - min_price
        print('min',min_price)
        print('max', max_price)

  return max_profit
      

prices1 = [15, 7, 9, 13, 45, 5]
the_prices = find_max_profit(prices1)
print(the_prices)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))