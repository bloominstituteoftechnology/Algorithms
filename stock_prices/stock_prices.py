#!/usr/bin/python
import argparse


def find_max_profit(prices):
    max_profit = 0
    if len(prices) < 2:
        return max_profit
    for buy in range(len(prices)):
        buy_price = prices[buy]
        for sell in range((buy), len(prices)-1):
            if sell <= len(prices):
                sell_price = prices[sell+1]
            else:
                sell_price = 0
            profit = sell_price - buy_price
            if max_profit == 0:   # set max_profit initial value
                max_profit = profit
            if profit > max_profit:
                max_profit = profit
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()
    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
