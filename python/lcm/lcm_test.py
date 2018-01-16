import unittest

from lcm import lcm

class LcmTests(unittest.TestCase):

    # def test_array_less_than_two(self):
    #      with self.assertRaisesWithMessage(ValueError):
    #         lcm([42])

    def test_calculates_lcm_with_two_numbers(self):
        self.assertIs(lcm([2, 3]), 6)
    
    def test_calculates_lcm_with_three_numbers(self):
        self.assertIs(lcm([2, 3, 4]), 12)
    
    def test_calculates_lcm_with_many_numbers(self):
        self.assertIs(lcm([2, 3, 4, 5, 6]), 60)

if __name__ == '__main__':
    unittest.main()
