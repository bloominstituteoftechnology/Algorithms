#!/usr/bin/python

import sys


def rock(arr, i):
    arr[i].append('rock')
    return arr


def paper(arr, i):
    arr[i].append('paper')
    return arr


def scissors(arr, i):
    arr[i].append('scissors')
    return arr


def rock_paper_scissors(n):
    rps = ['rock', 'paper', 'scissors']
    ans = [[] for i in range(3**n)]
    i = 0
    j = 0
    reps = 3**n
    while n:
        while i < reps:
            count = 0
            while count < int(3 ** (n-1)):
                ans[i].append(rps[j])
                i += 1
                count += 1
            j += 1
            count = 0
            while count < int(3 ** (n-1)):
                ans[i].append(rps[j])
                i += 1
                count += 1
            j += 1
            count = 0
            while count < int(3 ** (n-1)):
                ans[i].append(rps[j])
                i += 1
                count += 1
            j = 0
        n -= 1
        i = 0
    return ans


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')