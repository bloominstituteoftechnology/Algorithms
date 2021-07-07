#!/usr/bin/python

import argparse

def find_max_profit(prices):
  low = 0
  high = 0
  L = len(prices) - 1
  n = 0
  curr = 0
  next = 0
  #while n < L:
  curr = prices[n]
  next = prices[n+1]
  while n < L+1:
    if curr > next:
      if n < L:
        n +=1
        next = prices[n]
      else:
        break
    elif curr < next:
      curr = next
      n +=1
      next = prices[n]
  
  high = curr
  n = 0
  curr = prices[n]
  next = prices[n+1]
  while prices[n] != high:
    if curr > next:
      curr = next
      n +=1
      next = prices[n+1]
    elif curr < next:
      n +=1
      next = prices[n]

  profit = high - curr

  print(profit)
  #print(curr)
  #print(next)

  #create loop

  #find the largest value

  #find the smallest value to the left of the largest value

  #end loop

  #calculate the difference between the two elements
find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  #print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


