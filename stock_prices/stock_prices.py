#!/c/Users/Bryan/AppData/Local/Programs/Python/Python38/python

import argparse

def find_max_profit(prices):
  sell_price = 0
  buy_price = -1
  max_profit = -1
  for i in range(len(prices) -1):
    if buy_price == -1:
      buy_price = prices[i]
    if buy_price > prices[i]:
      buy_price = prices[i]
    for j in range(i, len(prices) -1):
      if prices[j] < prices[i+1] and sell_price < prices[i+1]:
        sell_price = prices[j+1]
    # if prices[i] < prices[i+1] and sell_price > prices[i+1]:
    #   sell_price = prices[i+1]
  max_profit = sell_price - buy_price
  return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  