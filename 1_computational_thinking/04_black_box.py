''' Black box
Black box testing is when we write the tests only knowing the input/output of a function, without see the code inside of it
'''

import unittest

def sum(num_1, num_2):
    return abs(num_1) + num_2


class BlackBoxTest(unittest.TestCase):

    def test_sum_two_positive(self):
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_two_negative(self):
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()
