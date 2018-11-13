#!/usr/bin/python

import argparse


def find_max_profit(prices):
    x = 0
    y = 0
    x = min(prices)

    if x == prices[-1]:  # if the lowest price is the last index
        y = min(prices[:-1])
        primary = -y + x  # difference of the 1st lowest number
        if prices[prices.index(y) + 1 : -1]:
            secondary = -y + max(
                prices[prices.index(y) + 1 : -1]
            )  # difference of 2nd lowest number
            return primary if primary > secondary else secondary
        return primary
    else:
        y = max(prices[prices.index(x) + 1 :])
        return y - x


# print(find_max_profit([10, 7, 5, 8, 11, 9])) #6
# print(find_max_profit([100, 90, 80, 50, 20, 10])) #-10
# print(find_max_profit([1050, 270, 1540, 3800, 2])) #3530
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])) #94

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

