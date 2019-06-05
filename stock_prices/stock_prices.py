#!/usr/bin/python

import argparse

'''
UNDERSTANDING:

Write algorithim to compute arr[i] - arr[:i] = most profitable/least loss

What is the range of the input?
  List of integers in an array that could be from anywhere from 1 to infinity

- Integer Only
- Input array is positive but return value can be negative
- arr[len(arr)-1] == the most recent price
- arr[0] == the oldest price 
- arr[i] == price in between oldest and most recent

------------------------------------------------------------------------------

PLANNING:
1.should loop through array 
2.index to the most right should subtract each number to the left of it
3.store all the values in an array
4.find the highest value in the array
5.return the the highest value as most profitable

'''
'''
PLANNING AFTER SOME GUIDANCE:

1) initialize max_profit
2) loop through array, consider the element you get each step as the current price
3) max value in the slice of the array starting from the index i+1 is the highest price you can sell the item at
4) calculate profit: highest_price - current_price and check if it's bigger than the actual max_profit
5) after you iterate over an entire array, return max_profit
'''

def find_max_profit(prices):
  current_price = 0
  max_profit = 'none'
  

  for i in range(len(prices)):
      current_price = prices[i]
      highest_price = prices[i+1:]
      for j in range(len(highest_price)):
          profit = highest_price[j]-current_price
          if(max_profit == 'none'):
              max_profit = profit
          elif(profit > max_profit):
              max_profit = profit

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))