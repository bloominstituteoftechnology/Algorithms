#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    result = []

    if n == 0:
        result.append([])
        return result

    def helper(arr, round):
        for i in range(len(plays)):
            arr.append(plays[i])
            if round == n:
                result.append(arr[i::1])
            else:
                helper(arr, round + 1)

    helper([], 1)
    return result


print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
