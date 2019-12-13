#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


"""
    understand
    ___________
    
    plan
    ___________
    
    search for biggest number in array, then search for smallest number in array that occurs before that biggest number
    Find the index of biggest number, make a subarray of all indexes before that biggest number and loop through that subarray
"""

def find_max_profit(arr):
    biggest_number_index = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[biggest_number_index]:
            biggest_number_index = i
    new_arr = arr[0: biggest_number_index]
    smallest_number_index = 0
    for i in range(0, len(new_arr)):
        if new_arr[i] < new_arr[smallest_number_index]:
            smallest_number_index = i

    return arr[biggest_number_index] - new_arr[smallest_number_index]

find_max_profit([1050, 270, 1540, 3800, 2])
