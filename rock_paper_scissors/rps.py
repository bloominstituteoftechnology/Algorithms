#!/usr/bin/env python

import sys


def rock_paper_scissors(n):
	if n == 0:
		return[[]]
	available_plays = ['rock', 'paper', 'scissors']
	plays = []
	for play in available_plays:
		for subplay in rock_paper_scissors(n - 1):
			plays.append(
				[play] + subplay
			)
	return plays


if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_plays = int(sys.argv[1])
		print(rock_paper_scissors(num_plays))
	else:
		print('Usage: rps.py [num_plays]')
