#!/usr/bin/python

import argparse


def find_max_profit(prices):
    highestDiff = 0
    lowestDiff = max(prices)-min(prices)
    for price in prices:
      profitArr = prices[prices.index(price):]
      if(max(profitArr) > price and ((max(profitArr) - price))> highestDiff ):
        highestDiff = (max(profitArr) - price)
      else:
        sortedPrices = sorted(profitArr) 
        if(len(sortedPrices)>=2):
          if(lowestDiff> sortedPrices[-1] - sortedPrices[-2]):
            lowestDiff = sortedPrices[-1] - sortedPrices[-2]
    if(highestDiff==0):
      return(lowestDiff * -1)
    return (highestDiff)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


