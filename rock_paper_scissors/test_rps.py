#!/usr/bin/env python

import unittest
from . import rock_paper_scissors


class Test(unittest.TestCase):

	def test_rock_paper_scissors_output(self):
		self.assertEqual(rock_paper_scissors(0), [[]])
		self.assertEqual(rock_paper_scissors(1), [['rock'], ['paper'], ['scissors']])
		self.assertEqual(rock_paper_scissors(2), [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']])
		self.assertEqual(rock_paper_scissors(3), [['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'], ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'], ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'], ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'], ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'], ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'], ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'], ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']])
		self.assertEqual(rock_paper_scissors(4), [['rock', 'rock', 'rock', 'rock'], ['rock', 'rock', 'rock', 'paper'], ['rock', 'rock', 'rock', 'scissors'], ['rock', 'rock', 'paper', 'rock'], ['rock', 'rock', 'paper', 'paper'], ['rock', 'rock', 'paper', 'scissors'], ['rock', 'rock', 'scissors', 'rock'], ['rock', 'rock', 'scissors', 'paper'], ['rock', 'rock', 'scissors', 'scissors'], ['rock', 'paper', 'rock', 'rock'], ['rock', 'paper', 'rock', 'paper'], ['rock', 'paper', 'rock', 'scissors'], ['rock', 'paper', 'paper', 'rock'], ['rock', 'paper', 'paper', 'paper'], ['rock', 'paper', 'paper', 'scissors'], ['rock', 'paper', 'scissors', 'rock'], ['rock', 'paper', 'scissors', 'paper'], ['rock', 'paper', 'scissors', 'scissors'], ['rock', 'scissors', 'rock', 'rock'], ['rock', 'scissors', 'rock', 'paper'], ['rock', 'scissors', 'rock', 'scissors'], ['rock', 'scissors', 'paper', 'rock'], ['rock', 'scissors', 'paper', 'paper'], ['rock', 'scissors', 'paper', 'scissors'], ['rock', 'scissors', 'scissors', 'rock'], ['rock', 'scissors', 'scissors', 'paper'], ['rock', 'scissors', 'scissors', 'scissors'], ['paper', 'rock', 'rock', 'rock'], ['paper', 'rock', 'rock', 'paper'], ['paper', 'rock', 'rock', 'scissors'], ['paper', 'rock', 'paper', 'rock'], ['paper', 'rock', 'paper', 'paper'], ['paper', 'rock', 'paper', 'scissors'], ['paper', 'rock', 'scissors', 'rock'], ['paper', 'rock', 'scissors', 'paper'], ['paper', 'rock', 'scissors', 'scissors'], ['paper', 'paper', 'rock', 'rock'], ['paper', 'paper', 'rock', 'paper'], ['paper', 'paper', 'rock', 'scissors'], ['paper', 'paper', 'paper', 'rock'], ['paper', 'paper', 'paper', 'paper'], ['paper', 'paper', 'paper', 'scissors'], ['paper', 'paper', 'scissors', 'rock'], ['paper', 'paper', 'scissors', 'paper'], ['paper', 'paper', 'scissors', 'scissors'], ['paper', 'scissors', 'rock', 'rock'], ['paper', 'scissors', 'rock', 'paper'], ['paper', 'scissors', 'rock', 'scissors'], ['paper', 'scissors', 'paper', 'rock'], ['paper', 'scissors', 'paper', 'paper'], ['paper', 'scissors', 'paper', 'scissors'], ['paper', 'scissors', 'scissors', 'rock'], ['paper', 'scissors', 'scissors', 'paper'], ['paper', 'scissors', 'scissors', 'scissors'], ['scissors', 'rock', 'rock', 'rock'], ['scissors', 'rock', 'rock', 'paper'], ['scissors', 'rock', 'rock', 'scissors'], ['scissors', 'rock', 'paper', 'rock'], ['scissors', 'rock', 'paper', 'paper'], ['scissors', 'rock', 'paper', 'scissors'], ['scissors', 'rock', 'scissors', 'rock'], ['scissors', 'rock', 'scissors', 'paper'], ['scissors', 'rock', 'scissors', 'scissors'], ['scissors', 'paper', 'rock', 'rock'], ['scissors', 'paper', 'rock', 'paper'], ['scissors', 'paper', 'rock', 'scissors'], ['scissors', 'paper', 'paper', 'rock'], ['scissors', 'paper', 'paper', 'paper'], ['scissors', 'paper', 'paper', 'scissors'], ['scissors', 'paper', 'scissors', 'rock'], ['scissors', 'paper', 'scissors', 'paper'], ['scissors', 'paper', 'scissors', 'scissors'], ['scissors', 'scissors', 'rock', 'rock'], ['scissors', 'scissors', 'rock', 'paper'], ['scissors', 'scissors', 'rock', 'scissors'], ['scissors', 'scissors', 'paper', 'rock'], ['scissors', 'scissors', 'paper', 'paper'], ['scissors', 'scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors', 'scissors']])
		self.assertEqual(rock_paper_scissors(5), [['rock', 'rock', 'rock', 'rock', 'rock'], ['rock', 'rock', 'rock', 'rock', 'paper'], ['rock', 'rock', 'rock', 'rock', 'scissors'], ['rock', 'rock', 'rock', 'paper', 'rock'], ['rock', 'rock', 'rock', 'paper', 'paper'], ['rock', 'rock', 'rock', 'paper', 'scissors'], ['rock', 'rock', 'rock', 'scissors', 'rock'], ['rock', 'rock', 'rock', 'scissors', 'paper'], ['rock', 'rock', 'rock', 'scissors', 'scissors'], ['rock', 'rock', 'paper', 'rock', 'rock'], ['rock', 'rock', 'paper', 'rock', 'paper'], ['rock', 'rock', 'paper', 'rock', 'scissors'], ['rock', 'rock', 'paper', 'paper', 'rock'], ['rock', 'rock', 'paper', 'paper', 'paper'], ['rock', 'rock', 'paper', 'paper', 'scissors'], ['rock', 'rock', 'paper', 'scissors', 'rock'], ['rock', 'rock', 'paper', 'scissors', 'paper'], ['rock', 'rock', 'paper', 'scissors', 'scissors'], ['rock', 'rock', 'scissors', 'rock', 'rock'], ['rock', 'rock', 'scissors', 'rock', 'paper'], ['rock', 'rock', 'scissors', 'rock', 'scissors'], ['rock', 'rock', 'scissors', 'paper', 'rock'], ['rock', 'rock', 'scissors', 'paper', 'paper'], ['rock', 'rock', 'scissors', 'paper', 'scissors'], ['rock', 'rock', 'scissors', 'scissors', 'rock'], ['rock', 'rock', 'scissors', 'scissors', 'paper'], ['rock', 'rock', 'scissors', 'scissors', 'scissors'], ['rock', 'paper', 'rock', 'rock', 'rock'], ['rock', 'paper', 'rock', 'rock', 'paper'], ['rock', 'paper', 'rock', 'rock', 'scissors'], ['rock', 'paper', 'rock', 'paper', 'rock'], ['rock', 'paper', 'rock', 'paper', 'paper'], ['rock', 'paper', 'rock', 'paper', 'scissors'], ['rock', 'paper', 'rock', 'scissors', 'rock'], ['rock', 'paper', 'rock', 'scissors', 'paper'], ['rock', 'paper', 'rock', 'scissors', 'scissors'], ['rock', 'paper', 'paper', 'rock', 'rock'], ['rock', 'paper', 'paper', 'rock', 'paper'], ['rock', 'paper', 'paper', 'rock', 'scissors'], ['rock', 'paper', 'paper', 'paper', 'rock'], ['rock', 'paper', 'paper', 'paper', 'paper'], ['rock', 'paper', 'paper', 'paper', 'scissors'], ['rock', 'paper', 'paper', 'scissors', 'rock'], ['rock', 'paper', 'paper', 'scissors', 'paper'], ['rock', 'paper', 'paper', 'scissors', 'scissors'], ['rock', 'paper', 'scissors', 'rock', 'rock'], ['rock', 'paper', 'scissors', 'rock', 'paper'], ['rock', 'paper', 'scissors', 'rock', 'scissors'], ['rock', 'paper', 'scissors', 'paper', 'rock'], ['rock', 'paper', 'scissors', 'paper', 'paper'], ['rock', 'paper', 'scissors', 'paper', 'scissors'], ['rock', 'paper', 'scissors', 'scissors', 'rock'], ['rock', 'paper', 'scissors', 'scissors', 'paper'], ['rock', 'paper', 'scissors', 'scissors', 'scissors'], ['rock', 'scissors', 'rock', 'rock', 'rock'], ['rock', 'scissors', 'rock', 'rock', 'paper'], ['rock', 'scissors', 'rock', 'rock', 'scissors'], ['rock', 'scissors', 'rock', 'paper', 'rock'], ['rock', 'scissors', 'rock', 'paper', 'paper'], ['rock', 'scissors', 'rock', 'paper', 'scissors'], ['rock', 'scissors', 'rock', 'scissors', 'rock'], ['rock', 'scissors', 'rock', 'scissors', 'paper'], ['rock', 'scissors', 'rock', 'scissors', 'scissors'], ['rock', 'scissors', 'paper', 'rock', 'rock'], ['rock', 'scissors', 'paper', 'rock', 'paper'], ['rock', 'scissors', 'paper', 'rock', 'scissors'], ['rock', 'scissors', 'paper', 'paper', 'rock'], ['rock', 'scissors', 'paper', 'paper', 'paper'], ['rock', 'scissors', 'paper', 'paper', 'scissors'], ['rock', 'scissors', 'paper', 'scissors', 'rock'], ['rock', 'scissors', 'paper', 'scissors', 'paper'], ['rock', 'scissors', 'paper', 'scissors', 'scissors'], ['rock', 'scissors', 'scissors', 'rock', 'rock'], ['rock', 'scissors', 'scissors', 'rock', 'paper'], ['rock', 'scissors', 'scissors', 'rock', 'scissors'], ['rock', 'scissors', 'scissors', 'paper', 'rock'], ['rock', 'scissors', 'scissors', 'paper', 'paper'], ['rock', 'scissors', 'scissors', 'paper', 'scissors'], ['rock', 'scissors', 'scissors', 'scissors', 'rock'], ['rock', 'scissors', 'scissors', 'scissors', 'paper'], ['rock', 'scissors', 'scissors', 'scissors', 'scissors'], ['paper', 'rock', 'rock', 'rock', 'rock'], ['paper', 'rock', 'rock', 'rock', 'paper'], ['paper', 'rock', 'rock', 'rock', 'scissors'], ['paper', 'rock', 'rock', 'paper', 'rock'], ['paper', 'rock', 'rock', 'paper', 'paper'], ['paper', 'rock', 'rock', 'paper', 'scissors'], ['paper', 'rock', 'rock', 'scissors', 'rock'], ['paper', 'rock', 'rock', 'scissors', 'paper'], ['paper', 'rock', 'rock', 'scissors', 'scissors'], ['paper', 'rock', 'paper', 'rock', 'rock'], ['paper', 'rock', 'paper', 'rock', 'paper'], ['paper', 'rock', 'paper', 'rock', 'scissors'], ['paper', 'rock', 'paper', 'paper', 'rock'], ['paper', 'rock', 'paper', 'paper', 'paper'], ['paper', 'rock', 'paper', 'paper', 'scissors'], ['paper', 'rock', 'paper', 'scissors', 'rock'], ['paper', 'rock', 'paper', 'scissors', 'paper'], ['paper', 'rock', 'paper', 'scissors', 'scissors'], ['paper', 'rock', 'scissors', 'rock', 'rock'], ['paper', 'rock', 'scissors', 'rock', 'paper'], ['paper', 'rock', 'scissors', 'rock', 'scissors'], ['paper', 'rock', 'scissors', 'paper', 'rock'], ['paper', 'rock', 'scissors', 'paper', 'paper'], ['paper', 'rock', 'scissors', 'paper', 'scissors'], ['paper', 'rock', 'scissors', 'scissors', 'rock'], ['paper', 'rock', 'scissors', 'scissors', 'paper'], ['paper', 'rock', 'scissors', 'scissors', 'scissors'], ['paper', 'paper', 'rock', 'rock', 'rock'], ['paper', 'paper', 'rock', 'rock', 'paper'], ['paper', 'paper', 'rock', 'rock', 'scissors'], ['paper', 'paper', 'rock', 'paper', 'rock'], ['paper', 'paper', 'rock', 'paper', 'paper'], ['paper', 'paper', 'rock', 'paper', 'scissors'], ['paper', 'paper', 'rock', 'scissors', 'rock'], ['paper', 'paper', 'rock', 'scissors', 'paper'], ['paper', 'paper', 'rock', 'scissors', 'scissors'], ['paper', 'paper', 'paper', 'rock', 'rock'], ['paper', 'paper', 'paper', 'rock', 'paper'], ['paper', 'paper', 'paper', 'rock', 'scissors'], ['paper', 'paper', 'paper', 'paper', 'rock'], ['paper', 'paper', 'paper', 'paper', 'paper'], ['paper', 'paper', 'paper', 'paper', 'scissors'], ['paper', 'paper', 'paper', 'scissors', 'rock'], ['paper', 'paper', 'paper', 'scissors', 'paper'], ['paper', 'paper', 'paper', 'scissors', 'scissors'], ['paper', 'paper', 'scissors', 'rock', 'rock'], ['paper', 'paper', 'scissors', 'rock', 'paper'], ['paper', 'paper', 'scissors', 'rock', 'scissors'], ['paper', 'paper', 'scissors', 'paper', 'rock'], ['paper', 'paper', 'scissors', 'paper', 'paper'], ['paper', 'paper', 'scissors', 'paper', 'scissors'], ['paper', 'paper', 'scissors', 'scissors', 'rock'], ['paper', 'paper', 'scissors', 'scissors', 'paper'], ['paper', 'paper', 'scissors', 'scissors', 'scissors'], ['paper', 'scissors', 'rock', 'rock', 'rock'], ['paper', 'scissors', 'rock', 'rock', 'paper'], ['paper', 'scissors', 'rock', 'rock', 'scissors'], ['paper', 'scissors', 'rock', 'paper', 'rock'], ['paper', 'scissors', 'rock', 'paper', 'paper'], ['paper', 'scissors', 'rock', 'paper', 'scissors'], ['paper', 'scissors', 'rock', 'scissors', 'rock'], ['paper', 'scissors', 'rock', 'scissors', 'paper'], ['paper', 'scissors', 'rock', 'scissors', 'scissors'], ['paper', 'scissors', 'paper', 'rock', 'rock'], ['paper', 'scissors', 'paper', 'rock', 'paper'], ['paper', 'scissors', 'paper', 'rock', 'scissors'], ['paper', 'scissors', 'paper', 'paper', 'rock'], ['paper', 'scissors', 'paper', 'paper', 'paper'], ['paper', 'scissors', 'paper', 'paper', 'scissors'], ['paper', 'scissors', 'paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper', 'scissors', 'paper'], ['paper', 'scissors', 'paper', 'scissors', 'scissors'], ['paper', 'scissors', 'scissors', 'rock', 'rock'], ['paper', 'scissors', 'scissors', 'rock', 'paper'], ['paper', 'scissors', 'scissors', 'rock', 'scissors'], ['paper', 'scissors', 'scissors', 'paper', 'rock'], ['paper', 'scissors', 'scissors', 'paper', 'paper'], ['paper', 'scissors', 'scissors', 'paper', 'scissors'], ['paper', 'scissors', 'scissors', 'scissors', 'rock'], ['paper', 'scissors', 'scissors', 'scissors', 'paper'], ['paper', 'scissors', 'scissors', 'scissors', 'scissors'], ['scissors', 'rock', 'rock', 'rock', 'rock'], ['scissors', 'rock', 'rock', 'rock', 'paper'], ['scissors', 'rock', 'rock', 'rock', 'scissors'], ['scissors', 'rock', 'rock', 'paper', 'rock'], ['scissors', 'rock', 'rock', 'paper', 'paper'], ['scissors', 'rock', 'rock', 'paper', 'scissors'], ['scissors', 'rock', 'rock', 'scissors', 'rock'], ['scissors', 'rock', 'rock', 'scissors', 'paper'], ['scissors', 'rock', 'rock', 'scissors', 'scissors'], ['scissors', 'rock', 'paper', 'rock', 'rock'], ['scissors', 'rock', 'paper', 'rock', 'paper'], ['scissors', 'rock', 'paper', 'rock', 'scissors'], ['scissors', 'rock', 'paper', 'paper', 'rock'], ['scissors', 'rock', 'paper', 'paper', 'paper'], ['scissors', 'rock', 'paper', 'paper', 'scissors'], ['scissors', 'rock', 'paper', 'scissors', 'rock'], ['scissors', 'rock', 'paper', 'scissors', 'paper'], ['scissors', 'rock', 'paper', 'scissors', 'scissors'], ['scissors', 'rock', 'scissors', 'rock', 'rock'], ['scissors', 'rock', 'scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors', 'rock', 'scissors'], ['scissors', 'rock', 'scissors', 'paper', 'rock'], ['scissors', 'rock', 'scissors', 'paper', 'paper'], ['scissors', 'rock', 'scissors', 'paper', 'scissors'], ['scissors', 'rock', 'scissors', 'scissors', 'rock'], ['scissors', 'rock', 'scissors', 'scissors', 'paper'], ['scissors', 'rock', 'scissors', 'scissors', 'scissors'], ['scissors', 'paper', 'rock', 'rock', 'rock'], ['scissors', 'paper', 'rock', 'rock', 'paper'], ['scissors', 'paper', 'rock', 'rock', 'scissors'], ['scissors', 'paper', 'rock', 'paper', 'rock'], ['scissors', 'paper', 'rock', 'paper', 'paper'], ['scissors', 'paper', 'rock', 'paper', 'scissors'], ['scissors', 'paper', 'rock', 'scissors', 'rock'], ['scissors', 'paper', 'rock', 'scissors', 'paper'], ['scissors', 'paper', 'rock', 'scissors', 'scissors'], ['scissors', 'paper', 'paper', 'rock', 'rock'], ['scissors', 'paper', 'paper', 'rock', 'paper'], ['scissors', 'paper', 'paper', 'rock', 'scissors'], ['scissors', 'paper', 'paper', 'paper', 'rock'], ['scissors', 'paper', 'paper', 'paper', 'paper'], ['scissors', 'paper', 'paper', 'paper', 'scissors'], ['scissors', 'paper', 'paper', 'scissors', 'rock'], ['scissors', 'paper', 'paper', 'scissors', 'paper'], ['scissors', 'paper', 'paper', 'scissors', 'scissors'], ['scissors', 'paper', 'scissors', 'rock', 'rock'], ['scissors', 'paper', 'scissors', 'rock', 'paper'], ['scissors', 'paper', 'scissors', 'rock', 'scissors'], ['scissors', 'paper', 'scissors', 'paper', 'rock'], ['scissors', 'paper', 'scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors', 'paper', 'scissors'], ['scissors', 'paper', 'scissors', 'scissors', 'rock'], ['scissors', 'paper', 'scissors', 'scissors', 'paper'], ['scissors', 'paper', 'scissors', 'scissors', 'scissors'], ['scissors', 'scissors', 'rock', 'rock', 'rock'], ['scissors', 'scissors', 'rock', 'rock', 'paper'], ['scissors', 'scissors', 'rock', 'rock', 'scissors'], ['scissors', 'scissors', 'rock', 'paper', 'rock'], ['scissors', 'scissors', 'rock', 'paper', 'paper'], ['scissors', 'scissors', 'rock', 'paper', 'scissors'], ['scissors', 'scissors', 'rock', 'scissors', 'rock'], ['scissors', 'scissors', 'rock', 'scissors', 'paper'], ['scissors', 'scissors', 'rock', 'scissors', 'scissors'], ['scissors', 'scissors', 'paper', 'rock', 'rock'], ['scissors', 'scissors', 'paper', 'rock', 'paper'], ['scissors', 'scissors', 'paper', 'rock', 'scissors'], ['scissors', 'scissors', 'paper', 'paper', 'rock'], ['scissors', 'scissors', 'paper', 'paper', 'paper'], ['scissors', 'scissors', 'paper', 'paper', 'scissors'], ['scissors', 'scissors', 'paper', 'scissors', 'rock'], ['scissors', 'scissors', 'paper', 'scissors', 'paper'], ['scissors', 'scissors', 'paper', 'scissors', 'scissors'], ['scissors', 'scissors', 'scissors', 'rock', 'rock'], ['scissors', 'scissors', 'scissors', 'rock', 'paper'], ['scissors', 'scissors', 'scissors', 'rock', 'scissors'], ['scissors', 'scissors', 'scissors', 'paper', 'rock'], ['scissors', 'scissors', 'scissors', 'paper', 'paper'], ['scissors', 'scissors', 'scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors', 'scissors', 'scissors']])


if __name__ == '__main__':
	unittest.main()
