#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # dp solution with memoization, bottom up solution
    cache = [[{} for _ in range(capacity+1)] for _ in range(len(items) + 1)]

    for i in range(len(items)+1):
        for s in range(capacity+1):
            if i == 0 or s == 0:
                cache[i][s] = {'Value': 0, 'Chosen': []}
            elif items[i-1].size > s:
                cache[i][s] = cache[i-1][s]
            else:
                test1 = cache[i-1][s]
                test2 = {'Value': cache[i-1][s-items[i-1].size]['Value'] + items[i-1].value,
                         'Chosen': cache[i-1][s-items[i-1].size]['Chosen'] + [items[i-1].index]}
                if test1['Value'] > test2['Value']:
                    cache[i][s] = test1
                else:
                    cache[i][s] = test2

    return cache[len(items)][capacity]

    # naive solution, top down, passes small tests, runtime on medium is too long so I stopped it
    # def helper(n, c, current_list, value):
    #     if n == 0 or c == 0:
    #         return {'Value': value, 'Chosen': current_list}
    #     elif items[n-1].size > c:
    #         ret = helper(n-1, c, current_list, value)
    #         return {'Value': ret['Value'], 'Chosen': ret['Chosen']}
    #     else:
    #         test1 = helper(n-1, c, current_list, value)
    #         test2 = helper(n-1, c - items[n-1].size, current_list + [items[n-1].index], value + items[n-1].value)
    #         if test1['Value'] > test2['Value']:
    #             return {'Value': test1['Value'], 'Chosen': test1['Chosen']}
    #         else:
    #             return {'Value': test2['Value'], 'Chosen': test2['Chosen']}
    #
    # res = helper(len(items), capacity, [], 0)
    # return {'Value': res['Value'], 'Chosen': sorted(res['Chosen'])}


"""
The value/weight ratio implementation is a greedy algorithm, which would work for some cases,
but won't fulfill many edge cases. In this case, a dynamic programming approach with memoization
would be superior to the greedy approach.
"""
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
