import unittest
from eating_cookies_naive import eating_cookies

class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    self.assertEqual(eating_cookies(0), 1)
    self.assertEqual(eating_cookies(1), 1)
    self.assertEqual(eating_cookies(2), 2)
    self.assertEqual(eating_cookies(5), 13)
    self.assertEqual(eating_cookies(10), 274)


if __name__ == '__main__':
  unittest.main()
