#!/usr/bin/python

import argparse

def find_max_profit(prices):
    biggest_change = 0 - max(prices) # set default value of return variable to lowest possible return value (so we can return negative values / losses)
    scratch_prices = prices.copy() # make a copy of the input so changes don't affect the input
    scratch_prices.append(0) # add an element on the end so that scratch_prices has an equal number of elements as prices
    for purchase_price in prices: # check one price against all prices after it
        scratch_prices.pop(0) # pop the first one (which we're checking) off of the scratch so it never returns 0 (needed to return negative values / losses)
        best_sale = max(scratch_prices) - purchase_price
        if best_sale > biggest_change:
            biggest_change = best_sale
        # for sale_price in scratch_prices: # this is from my naive solution
        #     change = sale_price - purchase_price # sale price minus purchase price
        #     if change > biggest_change: # keep it if it's bigger than the last stored value
        #         biggest_change = change
    return biggest_change


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
