import unittest
from making_change import coin_denominations

class Test(unittest.TestCase):

  def setUp(self):
    self.denominations = [1, 5, 10, 25, 100]

  def test_coin_denominations_small_amount(self):
    self.assertEqual(coin_denominations(0, self.denominations), 1)
    self.assertEqual(coin_denominations(1, self.denominations), 1)
    self.assertEqual(coin_denominations(5, self.denominations), 2)
    self.assertEqual(coin_denominations(10, self.denominations), 4)
    self.assertEqual(coin_denominations(20, self.denominations), 9)
    self.assertEqual(coin_denominations(30, self.denominations), 18)
    self.assertEqual(coin_denominations(100, self.denominations), 243)
    self.assertEqual(coin_denominations(200, self.denominations), 1706)
    self.assertEqual(coin_denominations(300, self.denominations), 6170)

  def test_coin_denominations_large_amount(self):
    self.assertEqual(coin_denominations(350, self.denominations), 10302)
    self.assertEqual(coin_denominations(400, self.denominations), 16215)
    self.assertEqual(coin_denominations(1000, self.denominations), 438966)
    self.assertEqual(coin_denominations(2000, self.denominations), 6142031)
    self.assertEqual(coin_denominations(5000, self.denominations), 220635826)
    self.assertEqual(coin_denominations(10000, self.denominations), 3430874151)


if __name__ == '__main__':
  unittest.main()