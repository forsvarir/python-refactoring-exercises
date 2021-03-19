import unittest
from dice_game import *

class TestDiceUtils(unittest.TestCase):
    def test_add_dice_returns_summation(self):
        self.assertEqual(3, add_dice(1, 2))
        