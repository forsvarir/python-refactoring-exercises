import unittest
from dice_game import *

class TestDiceUtils(unittest.TestCase):
    def test_add_dice_returns_summation(self):
        self.assertEqual(3, add_dice(1, 2))

    def test_calculate_score_even_roll_adds_ten(self):
        self.assertEqual(12, calculate_score(1, 1))