#!/usr/bin/python

import argparse

def find_max_profit(prices):

# track profit
  profit = min(prices) - max(prices)
# track index
  cur_high_index = 0
  cur_low_index = 0
# track high and low
  cur_high = 0
  cur_low = prices[cur_low_index]

  for i in range(len(prices)):
    # if it's lower than low and isn't the last item record it as the lowest item and record its index
    if prices[i] < cur_low and i != len(prices)-1:
      cur_low_index = i
      cur_low = prices[cur_low_index]
      print("newLow", cur_low)
      print("newLowIndex", cur_low_index)
    # if it's higher than high and comes after the lowest number, record it as the new high and record index
    if prices[i] > cur_high and i > cur_low_index:
      cur_high_index = i
      cur_high = prices[cur_high_index]
      print("newHigh", cur_high)
    # find profit from the highest and lowest that apply to params
    profit = cur_high - cur_low
  return profit

  

# profitFound = find_max_profit([1050, 270, 1540, 3800, 2])
# print(profitFound)

# profitFoundtwo = find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])
# print(profitFoundtwo)


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))