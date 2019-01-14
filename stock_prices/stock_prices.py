#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit = 0
    for cur, nxt in zip(prices, prices[1:]):
        buy_price = cur
        sell_price = nxt

        if sell_price < buy_price:
            buy_price = sell_price
            # sell_price = nxt

        profit = sell_price - buy_price
        print("buy", buy_price)
        print("sell", sell_price)
    # else:

    return profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

