import unittest
from moving_zeroes import moving_zeroes

class Test(unittest.TestCase):
    def test_moving_zeroes_return_value_1(self):
        arr = [0, 3, 1, 0, -2]
        answer = moving_zeroes(arr)

        self.assertEqual(len(answer), len(arr))

        for x in answer[:3]:
            self.assertTrue(x in arr)
            self.assertTrue(x != 0)

        for x in answer[3:]:
            self.assertEqual(x, 0)

    def test_moving_zeroes_return_value_2(self):
        arr = [1, 2, 3, 0, 4, 0, 0]
        answer = moving_zeroes(arr)

        for x in answer[:4]:
            self.assertTrue(x in arr)
            self.assertTrue(x != 0)

        for x in answer[4:]:
            self.assertEqual(x, 0)

    def test_moving_zeroes_return_value_3(self):
        arr = [4, 1, 2, 5]
        answer = moving_zeroes(arr)

        self.assertEqual(len(answer), len(arr)) 

        for x in answer:
            self.assertTrue(x in arr)
            self.assertTrue(x != 0)

    def test_moving_zeroes_return_value_4(self):
        arr = [0, 0, 0, 0, 0]
        answer = moving_zeroes(arr)

        self.assertEqual(len(answer), len(arr)) 

        for x in answer:
            self.assertTrue(x == 0)

    def test_moving_zeroes_return_value_5(self):
        arr = [0, 0, 0, 0, 3, 2, 1] 
        answer = moving_zeroes(arr)

        self.assertEqual(len(answer), len(arr)) 

        for x in answer[:3]:
            self.assertTrue(x in arr)
            self.assertTrue(x != 0)

        for x in answer[3:]:
            self.assertEqual(x, 0)


if __name__ == '__main__':
    unittest.main()