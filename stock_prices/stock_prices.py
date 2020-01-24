#!/usr/bin/python

import argparse

# Pull price one at a time, compare to previous price history (cache?) and compare max/min

# Have a running low number and a running high number and low must come before high


# BELOW COMES WITH NO PRINT STATEMENTS
def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0
    for i in range(len(prices)):
        current_price = prices[i]
        if current_price <= current_min_price_so_far and (0 < i < len(prices) - 1):
            profit = current_price - current_min_price_so_far
            current_min_price_so_far = current_price
            if profit >= max_profit_so_far:
                max_profit_so_far = profit
            if (profit <= max_profit_so_far) and i == 1:
                max_profit_so_far = profit
            else:
                pass
        elif current_price > current_min_price_so_far and (0 < i < len(prices) - 1):
            profit = current_price - current_min_price_so_far
            if profit >= max_profit_so_far:
                max_profit_so_far = profit
    return max_profit_so_far

# # BELOW COMES WITH MANY PRINT STATEMENTS
# def find_max_profit(prices):
#     current_min_price_so_far = prices[0]
#     max_profit_so_far = 0
#     for i in range(len(prices)):
#         # print('*******************************')
#         # print(f'FOR LOOP i = {i}')
#         current_price = prices[i]
#         # print(f'FOR LOOP CURRENT PRICE = {current_price}')
#         if current_price <= current_min_price_so_far and (0 < i < len(prices) - 1):
#             profit = current_price - current_min_price_so_far
#             current_min_price_so_far = current_price
#             # print(f'FIRST IF STATEMENT CURRENT MINIMUM PRICE SO FAR {current_min_price_so_far}')
#             # print(f'FIRST IF STATEMENT i = {i}')
#             if profit >= max_profit_so_far:
#                 max_profit_so_far = profit
#                 # print(f'SECOND IF STATEMENT MAX PROFIT SO FAR {max_profit_so_far}')
#             if (profit <= max_profit_so_far) and i == 1:
#                 max_profit_so_far = profit
#                 # print(f'THIRD IF STATEMENT MAX PROFIT SO FAR {max_profit_so_far}')
#             else:
#                 pass
#         elif current_price > current_min_price_so_far and (0 < i < len(prices) - 1):
#             profit = current_price - current_min_price_so_far
#             if profit >= max_profit_so_far:
#                 max_profit_so_far = profit
#                 # print(f'FOURTH IF STATEMENT CURRENT MINIMUM PRICE SO FAR {current_min_price_so_far}')
#                 # print(f'FOURTH IF STATEMENT i = {i}')
#                 # print(f'FOURTH IF STATEMENT MAX PROFIT SO FAR {max_profit_so_far}')
#     return max_profit_so_far


# prices1 = [100, 90, 80, 50, 20, 10]
# prices2 = [10, 7, 5, 8, 11, 9]
# prices3 = [1050, 270, 1540, 3800, 2]
# prices4 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
#
# print(find_max_profit(prices1))
# print(find_max_profit(prices2))
# print(find_max_profit(prices3))
# print(find_max_profit(prices4))


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#     args = parser.parse_args()
#
#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
