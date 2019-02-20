#!/usr/bin/python
import itertools
import sys
# essentially the input n is also going to be the number of elements in the inner array
# maybe make a dict that holds the strings as values and a number as a key
# rpsDict = {0: "rock", 1: "paper", 2:"scissors"}


def inner_recursion(n, rpsDict):
    return rpsDict[n]


def rock_paper_scissors(n):

    rpsDict = ['rock', 'paper', 'scissors']
    print(rpsDict[0])
    if n < 0:
        return [[]]
    elif n == 0:
        return [[]]
    else:
        listNew = itertools.product(rpsDict, repeat=n)
        lis = list(listNew)
        empty_list = []
        for index, x in enumerate(lis):
            empty_list.append(list(lis[index]))
        return empty_list

    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
