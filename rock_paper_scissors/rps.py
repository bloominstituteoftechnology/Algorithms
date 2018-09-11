#!/usr/bin/python

import argparse

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def generate_plays(rounds_left, result=[]):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for play in plays:
      generate_plays(rounds_left - 1, result + [play])

  generate_plays(n, [])
  return outcomes

if __name__ == '__main__':
  # This is just some code to input accepting inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
