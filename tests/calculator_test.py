import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # test that the add() method in calculator produces the correct results
        self.assertEqual(7, add(2, 5))

    def test_subtract(self):
        # test that the subtract() method performs as expected
        expected = 4
        actual = subtract(10, 6)
        self.assertEqual(expected, actual)