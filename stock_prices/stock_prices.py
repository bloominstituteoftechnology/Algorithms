#!/usr/bin/python
import argparse

def find_max_profit(prices):
  '''
  description:
    this function will find the max profit from buying/selling a stock

  pseudo: 
    - start with a loop
    - at the index compare the other values to the right of it, if the right value is greater it'll find the difference
      - add something to hold the profit value
    - the loop will continue and when it reaches another greater right value it'll return the profit and check if it's 
      greater than the previos profit value, which it'll then keep the greatest profit
    - it'll do this through the whole array until there is only one max profit
  '''
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))