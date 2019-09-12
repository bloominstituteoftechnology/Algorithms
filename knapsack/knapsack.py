#!/usr/bin/python

import sys
from collections import namedtuple

# For very very large lists, can implement binary search to find expected location

# def find_location(arr, target, idx=0):
#     if len(arr) == 0:
#         return -1  # empty array

#     if len(arr) == 1:
#         # if arr[0] is not target:
#         #   return -1
#         if arr[0]['ratio'] > target:
#             if idx - 1 < 0:
#                 return 0
#             return idx - 1
#         return idx

#     mid = len(arr) // 2

#     if arr[mid]['ratio'] >= target:
#         return idx + mid

#     next_arr = arr[:mid] if arr[mid]['ratio'] > target else arr[mid:]

#     if arr[mid]['ratio'] > target:
#         next_arr = arr[:mid]
#     else:
#         next_arr = arr[mid:]
#         idx = mid + idx

#     return find_location(next_arr, target, idx)

Item = namedtuple('Item', ['index', 'size', 'value'])

# Can I have two ratios that are the same?

# Get the ratio between value/cost
# sort by ratio >> create new sorted list
# loop over sorted ratios, adding to sack if current size + cost < total size
#   if current size + cost > total size, continue


def knapsack_solver(items, capacity):
    ratio_list = [{'ratio': -1}] * len(items)
    for item in items:
        index, size, value = [*item]
        ratio = item.value / item.size

        new_item = {
            'index': index,
            'size': size,
            'value': value,
            'ratio': ratio
        }

        # location = find_location(ratio_list, new_item['ratio'])
        # print(location, new_item['ratio'])
        # print(new_item['ratio'])

        # if location == -1:
        #     ratio_list.append(new_item)
        #     print(ratio_list)
        # else:
        #     ratio_list.insert(location, new_item)

        for index, value in enumerate(ratio_list):
            if value['ratio'] < new_item['ratio']:
                ratio_list.insert(index, new_item)
                break

    for item in ratio_list:
        print(f'l: {item["ratio"]}')


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