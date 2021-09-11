''' Glass box
Glass box testing is when we write the tests knowing how is code the function, trying every branch case for the code
'''

import unittest

def is_adult(age):
    if age >= 18:
        return False
    else:
        return False


class GlassBoxTest(unittest.TestCase):

    def test_is_adult(self):
        age = 20
        result = is_adult(age)
        self.assertEqual(result, True)

    def test_is_not_adult(self):
        age = 15
        result = is_adult(age)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()