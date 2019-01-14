#!/usr/bin/python

import argparse


def find_max_profit(prices):
    list_to_sum = []
    for i in prices:
        try:
            if prices[i] < prices[i + 1]:
                print(
                    f'Gap between {prices[i]} and {prices[i + 1]} is a profit at {prices[i + 1] - prices[i]}')
                list_to_sum.append(prices[i + 1] - prices[i])
            else:
                print(f'fadsfasfasdfasdf')
        except:
            pass
    return sum(list_to_sum)


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
