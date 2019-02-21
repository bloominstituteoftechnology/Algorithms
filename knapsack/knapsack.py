#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


class Combo:
    def __init__(self, value=0, size=0, items=[]):
        self.value = value
        self.size = size
        self.items = items

    def add_item(self, item):
        (index, size, value) = item
        print(self.items)

        return Combo(
            value=self.value + value,
            size=self.size + size,
            items=self.items + [index]
        )

    def __repr__(self):
        return 'value: {}, size: {}, items: {}'.format(self.value, self.size, self.items)


empty_sack = Combo()


def knapsack_solver(items, capacity):
    items = sorted(items, key=lambda item: item.size)
    cache = {}

    smallest_size = items[0].size

    if smallest_size > capacity:
        return 'Too small'
    best_seen = Combo()

    # items loop
    for i in range(len(items)):
        item = items[i]
        print(item)
        (index, size, value) = item
        # print(item)
        # print(smallest_size, capacity + 1)

        # capacity loop
        for space in range(smallest_size, capacity + 1):
            if space == 50 and index == 5:
                return
            # loop through prior items and find largest possible combo
            # from adding on this item

            remaining_space = space - size
            if remaining_space < 0:
                continue

            best_fitting = cache.get(remaining_space, empty_sack)

            if best_seen.value < best_fitting.value + value and item.index not in best_fitting.items:
                new_best = best_fitting.add_item(item)
                print('>>>>>>>>>>>>>>>>>>')
                print('cache')
                for line in sorted(list(cache)):
                    print(line, ':', cache[line])
                print(best_fitting)
                print(item, space)
                print('item', item, 'space', space, 'remaining space', remaining_space,
                      'old', best_seen, 'new', new_best)
                best_seen = new_best

            cache[space] = best_seen

    print(cache)
    best = cache[capacity]
    print(best)
    return {'Value': best.value, 'Chosen': sorted(best.items)}


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
