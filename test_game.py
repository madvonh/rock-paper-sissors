import unittest
from unittest.mock import patch

import game


class TestDetermineWinner(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(game.determine_winner("rock", "rock"), "tie")

    def test_user_win(self):
        self.assertEqual(game.determine_winner("paper", "rock"), "win")

    def test_user_lose(self):
        self.assertEqual(game.determine_winner("scissors", "rock"), "lose")


class TestGameFlow(unittest.TestCase):
    @patch("game.random.choice", return_value="scissors")
    @patch("builtins.input", side_effect=["rock", "no"])
    @patch("builtins.print")
    def test_single_round_win_and_exit(self, print_mock, _input_mock, _choice_mock):
        game.game()

        print_mock.assert_any_call("Welcome to Rock, Paper, Scissors!")
        print_mock.assert_any_call("Computer chose: scissors")
        print_mock.assert_any_call("You win!")
        print_mock.assert_any_call("Thanks for playing! Goodbye!")

    @patch("game.random.choice", return_value="scissors")
    @patch("builtins.input", side_effect=["lizard", "rock", "no"])
    @patch("builtins.print")
    def test_invalid_choice_then_retry(self, print_mock, _input_mock, _choice_mock):
        game.game()

        print_mock.assert_any_call("Invalid choice. Please try again.")
        print_mock.assert_any_call("Computer chose: scissors")
        print_mock.assert_any_call("You win!")
        print_mock.assert_any_call("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    unittest.main()
