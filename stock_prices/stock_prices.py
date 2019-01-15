#!/usr/bin/python
import math
import argparse


# def find_max_profit(prices):
    
#     max_profit = float("inf")

#     while prices != []:
#         bought = prices[0]

#         for p in prices[1:]:
#             profit = p - bought
#             if profit > max_profit:
#                 max_profit = profit
        
#         prices.pop(0)
    
#     print(max_profit)

def find_max_profit(prices):
    min_buy_price = prices[0]
    max_profit = prices[1] - min_buy_price

    for p in prices[1:]:
        profit = p - min_buy_price

        max_profit = max(profit, max_profit)
        min_buy_price = min(p, min_buy_price)
    
    return max_profit



# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))

prices = [100, 113, 110, 85, 105, 102, 86,
          63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print(find_max_profit(prices))
# print(max(find_max_profit([1050, 270, 1540, 3800, 2])))
# print(max(find_max_profit([10, 7, 5, 8, 11, 9])))
