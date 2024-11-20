# test_math_operations.py
import unittest
from math_operations import addition

class TestMathOperations(unittest.TestCase):
    def test_addition(self):  # Correctement indenté
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
