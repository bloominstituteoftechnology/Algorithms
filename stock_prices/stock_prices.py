#!/usr/bin/python

import argparse


def find_max_profit(prices):
  min_price = min(prices)
  min_i = prices.index(min_price)
  max_price = max(prices)
  max_i = prices.index(max_price)
  sorted_price = sorted(prices)
  t_f = []
  check = prices[1:]
  if max_i == 0:
    max_price = sorted_price[-2]
  profit = max_price - min_price
  if min_i == len(prices)-1:
    check.remove(min_price)
    previous = prices[0]
    for price in check:
      if previous > price:
        t_f.append(True)
        previous = price
      else:
        t_f.append(False)
        previous = price
    if t_f.count(False) == 0:
      return(sorted_price[-2]-sorted_price[-1])
    else:
      return(max_price-sorted(check)[0])
  else:
    return(profit)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))