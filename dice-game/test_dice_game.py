import unittest
from dice_game import *

class TestDiceUtils(unittest.TestCase):
    def test_add_dice_returns_summation(self):
        self.assertEqual(3, add_dice(1, 2))

    def test_calculate_score_even_roll_adds_ten(self):
        self.assertEqual(12, calculate_score(1, 1))

    def test_calculate_score_odd_roll_loses_5(self):
        self.assertEqual(6, calculate_score(6, 5))

    def test_calculate_score_low_odd_roll_minimum_zero(self):
        self.assertEqual(0, calculate_score(1,2))
        
    def test_calculate_score_roll7_scores2(self):
        self.assertEqual(2, calculate_score(5,2))
        
    def test_calculate_score_roll5_scores0(self):
        self.assertEqual(0, calculate_score(3,2))