#!/usr/bin/python

# prices = [1050, 270, 1540, 3800, 2]

import argparse


# def find_max_profit(prices):
#     min_price = prices[0]
#     max_price = prices[0]
#     max_price_diff = 0

#     for price in prices:
#         min_price = min(price, min_price)
#         if price > max_price:
#             max_price_diff = max(max_price_diff, price - min_price)
#             # max_price = price

#         return max_price_diff

def find_max_profit(prices):
    prices_size = len(prices)

    max_diff = prices[1] - prices[0]

    for i in range(0, prices_size):
        for j in range(i+1, prices_size):
            if(prices[j] - prices[i] > max_diff):
                max_diff = prices[j] - prices[i]

    return max_diff


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

    # Need to iterate through the list and compare the deltas. When one delta is larger than the prev
    # discard prev and keep new. Continue comparison. Bubble sort?
