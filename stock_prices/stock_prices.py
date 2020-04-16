#!/usr/bin/python

### whats the problem we have a list of numbers, and we need to check which number is the biggest in the list then store and compare
## this index to the number with the lowest index and then take the lowest from the highest

import argparse

def find_max_profit(prices):
    mp = [0] ## set max profit to initial 0 

    for i in range(0, len(prices) -1): ## getting the initial value from mp to the last element
      ci = i ## define index

      for x in range(ci + 1, len(prices) -1): ## initiate the check from initial index to last index -1
        if prices[x] - prices[ci] > mp[0]: ## subtract current index from the index we have in prices 
          mp[0] = prices[x] - prices[ci]

        elif prices[x] - prices[ci] < 0 and mp[0] == 0: ## if we hit negative numbers 
          mp[0] = prices[x] - prices[ci]

    return mp[0]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))