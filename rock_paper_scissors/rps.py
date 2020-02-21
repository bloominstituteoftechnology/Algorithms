#!/usr/bin/python

import sys

# define valid moves.....no 'spock', 'monster' etc.
validMoves = [['rock'], ['paper'], ['scissors']]


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    if n == 1:
        return validMoves

        output = []
        arr = rock_paper_scissors(n - 1)
        for subArr in arr:
            for move in validMoves:
                newMove = subArr + move
                output.append(newMove)
        return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
