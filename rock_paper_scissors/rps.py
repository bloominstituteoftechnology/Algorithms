#!/usr/bin/python

import sys

plays = ('rock', 'paper', 'scissors')

def rock_paper_scissors(n):
    results = []
    if n == 0:
        return [[]]
    if n == 1:
        results = [[play] for play in plays]
    if n > 1:
        for play in plays:
            current = [play]
            for item in rock_paper_scissors(n-1):
                current.extend(item)
                results.append(current)
                current = [play]
    return results
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')