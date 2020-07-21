import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # test that the add() method in calculator produces the correct results
        self.assertEqual(7, add(2, 5))