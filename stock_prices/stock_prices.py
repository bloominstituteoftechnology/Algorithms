#!/usr/bin/python

import argparse

def find_max_profit(prices):
    min = prices[0]
    p = None
    for i in range(1,len(prices)):
        if (prices[i] - min) > p if p != None else True:
            p = prices[i] - min 
        if prices[i] < min:
            min = prices[i]
        
    return p


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))