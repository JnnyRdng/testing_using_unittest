import unittest
from src.calculator import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # test that the add() function in calculator produces the correct results
        expected = 7
        actual = add(2, 5)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        # test that the subtract() function performs as expected
        expected = 4
        actual = subtract(10, 6)
        self.assertEqual(expected, actual)

    def test_divide(self):
        # test for divide function
        expected = 3
        actual = divide(21, 7)
        self.assertEqual(expected, actual)

    def test_multiply(self):
        # test multiply
        expected = 12
        actual = multiply(3, 4)
        self.assertEqual(expected, actual)

    # integration
    def test_more_than_one_operation(self):
        # test mutiple functions producing a single output
        expected = 49
        num_1 = add(4, 3)
        num_2 = subtract(9, 2)
        actual = multiply(num_1, num_2)
        self.assertEqual(expected, actual)

