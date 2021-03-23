from dice_game import add_dice
from dice_game import calculate_score
from dice_game import is_valid_name
from dice_game import evaluate_winner
from dice_game import Player
import collections
import unittest

class TestDiceUtils(unittest.TestCase):
    def test_add_dice_returns_summation(self):
        self.assertEqual(3, add_dice(1, 2))

    def test_calculate_score_even_roll_adds_ten(self):
        self.assertEqual(14, calculate_score(3, 1))

    def test_calculate_score_odd_roll_loses_5(self):
        self.assertEqual(6, calculate_score(6, 5))

    def test_calculate_score_low_odd_roll_minimum_zero(self):
        self.assertEqual(0, calculate_score(1,2))
        
    def test_calculate_score_roll7_scores2(self):
        self.assertEqual(2, calculate_score(5,2))
        
    def test_calculate_score_roll5_scores0(self):
        self.assertEqual(0, calculate_score(3,2))

    def test_calculate_score_roll_double_adds_ten_and_new_roll(self):
        self.assertEqual(17, calculate_score(1,1, lambda:5))

    def test_is_valid_for_valid_name(self):
        names = ["player"]
        self.assertTrue(is_valid_name(names, "player"))

    def test_is_valid_for_valid_name_end_of_list(self):
        names = ["p1", "p2", "p3", "p4", "valid player"]
        self.assertTrue(is_valid_name(names, "valid player"))

    def test_id_valid_invalid_name(self):
        names = ["p1", "p2"]
        self.assertFalse(is_valid_name(names, "invalid player"))

    def test_evaluate_winner_player1_high_score(self):
        winning_player = evaluate_winner(Player("player1", 100), Player("player2", 1))
        self.assertEqual("player1", winning_player.name)

    def test_evaluate_winner_player2_high_score(self):
        winning_player = evaluate_winner(Player("player1", 5), Player("player2", 10))
        self.assertEqual("player2", winning_player.name)

    def test_evaluate_winner_draw_player1_wins_rolloff(self):
        rolls = collections.deque([5, 1])

        winning_player = evaluate_winner(Player("player1", 1), Player("player2", 1), lambda : rolls.popleft())
        self.assertEqual("player1", winning_player.name)

    def test_evaluate_winner_draw_player2_wins_rolloff(self):
        rolls = collections.deque([1, 1, 2, 4])
        winning_player = evaluate_winner(Player("player1", 1), Player("player2", 1), lambda : rolls.popleft())
        self.assertEqual("player2", winning_player.name)
