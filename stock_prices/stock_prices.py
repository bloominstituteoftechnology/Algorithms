#!/usr/bin/python

import argparse

def find_max_profit(prices):
    i = 0
    maxprofit = -10000000000

    for price in prices:
        if i < len(prices) - 1:
            if prices[i+1] > price:

                    high = max(prices[i:])
                    profit = high - price
                    if profit > maxprofit:
                        maxprofit = profit
        if price == prices[-1] and maxprofit == -10000000000:
            maxprofit = 0 - price
        i = i + 1

    print('result', maxprofit)
    return maxprofit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
