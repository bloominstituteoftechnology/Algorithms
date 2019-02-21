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
    cache = [None] * len(items)

    smallest_size = items[0].size

    if smallest_size > capacity:
        return 'Too small'
    best_seen = Combo()

    # set up first row
    cache[0] = {}
    for space in range(smallest_size, capacity + 1):
        cache[0][space] = Combo().add_item(items[0])

    # items loop
    for i in range(1, len(items)):
        cache[i] = {}
        item = items[i]
        (index, size, value) = item
        # print(item)

        for space in range(smallest_size, capacity + 1):
            # first col, either the last row's first col, or just this item, depending on what's larger
            if space == smallest_size:
                if item.value > cache[i - 1][space].value:
                    cache[i][space] = Combo().add_item(item)
                else:
                    cache[i][space] = cache[i - 1][space]

            # loop through prior items and find largest possible combo
            # from adding on this item
            else:

                # find out how much space is left at this amount of space after this item is deducted
                remaining_space = space - size

                # if there is too little space, use prior best value
                if remaining_space < smallest_size:
                    cache[i][space] = cache[i - 1][space]

                # otherwise compare value to left, to this item.value + the optimal use of remaining space
                else:

                    best_fitting = cache[i - 1][remaining_space]
                    best_seen = cache[i - 1][space]

                    if best_seen.value < best_fitting.value + value:
                        new_best = best_fitting.add_item(item)
                        best_seen = new_best

                    cache[i][space] = best_seen

    best = cache[-1][capacity]
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
