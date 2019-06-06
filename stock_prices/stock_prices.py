#!/usr/bin/python
# what are stock prices and 
# stock price
# to find max profit 
# we need min or maybe lets call it
# set the profit
# set the min_profit which is min
# declare the value in price
# get the profit  
# min and max 
# profit will be the differne between 
import argparse

def find_max_profit(prices):
    profit = 0
    min = prices[0]
    for i in prices:
        val = i
        print(f"val: {val}")
        if val < min:
            min = val
            if val == prices[len(prices) - 1] and profit == 0:
                profit = profit - min
        elif val > min and profit < val - min:
            profit = val - min
            print(f"min: {min} and profit: {profit}")
    return profit


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

