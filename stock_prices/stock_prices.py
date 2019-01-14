#!/usr/bin/python

import argparse

highnum = []
lownum = []
complist = []

def find_max_profit(prices):
  for price in prices:
    if price - [price] > 0:
      append(lownum)
    if price - [price] < 0:
      append(highnum)  
  for i in highnum:
    for n in lownum:
      highnum[i] > lownum[n]
      complist.append([i]-[n])
  print (complist)
  pass 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))