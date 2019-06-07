#!/usr/bin/python

# Buy implies a negative value, sell implies a positive value
# You can only sell if you have bought, no short-selling
# Max Profit is selling at the highest point after buying at the lowest point that preceded it. 

import argparse

def find_max_profit(prices):
    max_profit = 0
    bot = 0
    sold = 0
    profit = []
  
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            bot = -prices[i]
            sold = prices[j]
            profit.append(bot + sold)
            # if profit > max_profit:
            #     max_profit, profit = profit, max_profit # SWAP
            max_profit = max(profit)

    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A max profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))