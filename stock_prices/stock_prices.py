#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # min_buy = min(prices)
    # max_sell = max(prices)
    # min_buy = 10000
    # max_buy = [0, 2]
    # index = 0
    # for i in prices:
    #
    #     if i > max_buy[0] and index > 0:
    #         max_buy[0] = i
    #         max_buy[1] = index
    #         print("MAX", max_buy[0])
    #
    #     if i < min_buy and index < max_buy[1]:
    #         min_buy = i
    #         print("MIN:", min_buy)
    #     index += 1
    #
    # return max_buy[0] - min_buy
    max_profit = -10 # Yes there was a work around
    min_buy = 0
    sell_price = 0
    change_buy_index = True

    for i in range(0, len(prices) - 1):  # this is so i doesn't go out of range on line 31
      sell_price = prices[i + 1]
      if change_buy_index:
        min_buy = prices[i]
      if sell_price < min_buy:
        change_buy_index = True
        continue
      else:
        temp_profit = sell_price - min_buy
        if temp_profit > max_profit:
          max_profit = temp_profit
        change_buy_index = False

    return max_profit




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))