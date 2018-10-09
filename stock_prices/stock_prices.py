#!/usr/bin/python

import argparse
import math


diff = []


def find_max_profit(prices):
    global diff
    diff = []

    for i in prices:
        find_diff(i, prices)

    diff.sort()
    return (diff[len(diff)-1])   
       

def find_diff(a, prices):
    global diff
    
    for j in prices:
        if prices.index(a) < prices.index(j):
            diff.append(j-a)




if __name__ == '__main__':
  #This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
