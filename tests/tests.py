import unittest
from modules import calculations

class TestSquareFunction(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(calculations.squares([4], [16]))

    def test_square_zero(self):
        self.assertEqual(calculations.squares([0], [0]))

    def test_square_negative(self):
        self.assertEqual(calculations.squares([-3], [9]))

if __name__ == '__main__':
    
    numbers = [1, 2, 3, 4, 5]

    print(calculations.squares(numbers))