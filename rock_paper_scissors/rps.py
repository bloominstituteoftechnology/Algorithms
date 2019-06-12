#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [['r'], ['p'], ['s']]
    else:
        l = []
        for i in rock_paper_scissors(n-1):
            l = l + [i + ['r'], i + ['p'] + i + ['s']]

    return l


# l=[1,2,3]
# print(rock_paper_scissors(2))


# def helper_fun(l):
#     plays = [['r'], ['p'], ['s']]
#     l2 = []
#     for x in l:
#         for i in plays:
#             l2.append(x + i)
#     return l2


print(rock_paper_scissors(4))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
