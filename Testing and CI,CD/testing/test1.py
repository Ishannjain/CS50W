import unittest
from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_prime(3))
    def test_2(self):
        self.assertTrue(is_prime(2))
    def test_3(self):
        self.assertFalse(is_prime(3))
    if __name__=="__main__":
        unittest.main()