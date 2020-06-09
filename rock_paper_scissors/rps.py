#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        plays = rock_paper_scissors(1)
        for i in range(n-1):
            new_plays = []
            for move_list in plays:
                for move in rock_paper_scissors(1):
                    new_plays += [move_list + move]
            plays = new_plays
        return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')