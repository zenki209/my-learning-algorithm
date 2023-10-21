import unittest
from thewidestpath import solution


class TestSum(unittest.TestCase):
    def test_1(self):

        X = [5,5,5,7,7,7]
        Y = [3,4,5,1,3,7]
        result = solution(X, Y)
        self.assertEqual(result, 2)
    


if __name__ == '__main__':
    unittest.main()