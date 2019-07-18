#!/usr/bin/python

import sys

options = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    result = [[] for i in range(3**n)]

    def gamePlay(p):
        if p == 0:
            return

        count = 0
        while count < 3**n:
            for i in range(3**p//3):
                result[count].append('rock')
                count += 1
            for i in range(3**p//3):
                result[count].append('paper')
                count += 1
            for i in range(3**p//3):
                result[count].append('scissors')
                count += 1
        gamePlay(p - 1)
    gamePlay(n)

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
