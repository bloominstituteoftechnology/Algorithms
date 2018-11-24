import unittest
from climbing_stairs import climbing_stairs

class Test(unittest.TestCase):
  print('--- NEW TEST SUITE ---')
  def test_climbing_stairs_small_n(self):
    print('--- TESTS FOR SMALL n ---\n')
    print('--- TEST n = 0 ---\n')
    self.assertEqual(climbing_stairs(0), 1)
    print('--- TEST n = 1 ---\n')
    self.assertEqual(climbing_stairs(1), 1)
    print('--- TEST n = 2 ---\n')
    self.assertEqual(climbing_stairs(2), 2)
    print('--- TEST n = 5 ---\n')
    self.assertEqual(climbing_stairs(5), 13)
    print('--- TEST n = 10 ---\n')
    self.assertEqual(climbing_stairs(10), 274)

  def test_climbing_stairs_large_n(self):
    print('--- TESTS FOR LARGE n ---')
    print('--- TEST n = 50 ---\n')
    self.assertEqual(climbing_stairs(50, [0 for i in range(51)]), 10562230626642)
    print('--- TEST n = 100 ---\n')
    self.assertEqual(climbing_stairs(100, [0 for i in range(101)]), 180396380815100901214157639)
    print('--- TEST n = 500 ---\n')
    self.assertEqual(climbing_stairs(500, [0 for i in range(501)]), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__': 
  unittest.main()

  