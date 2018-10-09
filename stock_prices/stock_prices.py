#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buying = True
  buyprice = 0
  highest = 0
  lowest = 0
  for i in range(len(prices)-1):
    if buying:
      if prices[i] < prices[i+1]:
        buyprice = prices[i]
        buying = False
      else:
        pass
    elif not buying:
      if prices[i] > prices[i+1]:
        if prices[i] - buyprice > highest:
          highest = prices[i]-buyprice
          buyprice = 0
          buying = True
        else:
          pass
      else:
        pass
  return -10 if highest == 0 else highest
  # profit = max(sell - buy for buy, sell in itertools.combinations(prices, 2))
  # return profit

if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))