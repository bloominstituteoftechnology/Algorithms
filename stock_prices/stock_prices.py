#!/usr/bin/python

import argparse
                      # list of 4
def find_max_profit(prices):
  #Find the max value in the prices list
  sell_value = max(prices)
  # Get the index of max/sell in the prices list
  sell_index = prices.index(sell_value)
  # Slice the prices list after selling value(Min value) 
  # if the sell value is the beginning of the list then ignore it consider the value after it 
  if sell_index == 0:
    sell_value = max(prices[1:])
    sell_index = prices.index(sell_value)

  sell_index = prices.index(sell_value)  
  sliced_list = prices[0:sell_index]  
  
  print(sliced_list)
  #Find the maximum value in the prices list after min value
  buy_value = min(sliced_list) 
  # print(sell_value)
  # Find the profit by subtracting the min from max price
  profit = sell_value - buy_value
  
  #return the profit
  return profit
  # print(profit)

# find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))