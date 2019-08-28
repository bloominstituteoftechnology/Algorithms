#!/usr/bin/python

import argparse

def find_max_profit(prices):
    counter = 0
    # prices_copy = prices[:]
    # elif counter == len(prices) - 1:
    new_copy = prices[:]
    final_arr = []
    count = 0 
    for num in new_copy:
        count += 1
        for i in range((count - 1), len(new_copy) - 1):
            if i < len(new_copy) - 1:
                test = num - new_copy[i + 1]
                final_arr.append((num, new_copy[i+1]))
            else:
                pass
    # print(final_arr)
    sec_arr = []
    if len(final_arr) > 0:
        for tup in final_arr:
            # print(tup[0], tup[1])
            if tup[0] < tup[1]:
                result = tup[1] - tup[0]
                sec_arr.append(result)
        # print(sec_arr)
        if len(sec_arr) > 0:
            final = max(sec_arr)
            return final
        else:
            for tup in final_arr:
                # print(tup[0], tup[1])
                if tup[0] > tup[1]:
                    result = tup[1] - tup[0]
                    sec_arr.append(result)
            final = max(sec_arr)
            return final

        # working_nums = filter(lambda x: x > 0, final_arr)
        # new_min = min(working_nums)
        # new_min = new_min * -1
        # # print(new_min)
        # return new_min




# stock_prices_one = [100,55,4,98,10,18,90,95,43,11,47,67,89,42,49,79]
# stock_prices_two = [10,7,5,8,11,9]
# stock_prices_three = [100, 90,80,50,20,10]
# find_max_profit(stock_prices_one)
# find_max_profit(stock_prices_two)
# find_max_profit(stock_prices_three)
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
#
#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
