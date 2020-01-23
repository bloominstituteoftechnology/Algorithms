#!/usr/bin/python
import argparse


def find_max_profit(prices):

    # save min idx, max idx
    min_idx = 0
    max_idx = len(prices)-1

    # loop through the arr without last index, find the smallest
    for i in range(len(prices)-1):
        if prices[min_idx] > prices[i]:
            min_idx = i

    # loop spliced array from min idx
    for i in range(min_idx+1, len(prices)-1):
        if prices[max_idx] < prices[i]:
            max_idx = i

    # return max difference between max and min
    return prices[max_idx] - prices[min_idx]


    # better time complexity:
    # save high and low,
    # set low as first item, high as last item
    # save indexes for high and low
    # iterate through left to right
    # if high idx > low idx & high > low, save highs
    # if low idx < high idx & low < high, save lows
    # return high - low

    # current_min_price_so_far = prices[0]
    # max_profit_so_far = prices[len(prices)-1]
    # prit(max_profit_so_far)

    # for i in range(len(prices)):

    #     high = prices[len(prices)-1]



if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
