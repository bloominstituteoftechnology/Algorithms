#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cur_max_index = 0
  cur_low_index = 0
  cur_max = 0
  print("cur_max", cur_max)
  cur_low = prices[cur_low_index]
  print("cur_low", cur_low)

  for price in range(len(prices)):
    profit = cur_max - cur_low

    print("profit", profit)
    if prices[price] > cur_max and price > cur_low_index:
      cur_max_index = price
      cur_max = prices[cur_max_index]
      print("new cur max num", cur_max)

    elif prices[price] < cur_low and price != len(prices) - 1:
      cur_low_index = price
      cur_low = prices[cur_low_index]
      print("new cur low price", prices[cur_low_index])


  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))