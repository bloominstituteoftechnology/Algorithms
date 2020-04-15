#!/usr/bin/python

import argparse

def find_max_profit(prices):
    differences = []
      # go through the prices and find the greatest difference between prices[x] and prices[y] where x > y 
    for x in range(0, len(prices)):
        for y in range(0, len(prices)):
            if x > y:
                difference = prices[x] - prices[y], x, y
                differences.append(difference)
    return max(differences)[0]

    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))