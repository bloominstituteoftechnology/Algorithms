#!/usr/bin/python
import argparse


def find_max_profit(prices):
  # brute force:
  # save max difference
  # iterate through the arr
  # sub loop to iterate through the rest starting at next i
  # return max difference

  # better time complexity:
  # save high and low,
  # set low as first item, high as last item
  # save indexes for high and low
  # iterate through left to right
  # if high idx > low idx & high > low, save highs
  # if low idx < high idx & low < high, save lows
  # return high - low


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(
    description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(
    profit=find_max_profit(args.integers), prices=args.integers))
