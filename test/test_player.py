import unittest
from unittest.mock import MagicMock
from player import ComputerPlayer
from player import HumanPlayer
from match_pile import MatchPile


class TestComputer(unittest.TestCase):
    def pick_match(self, matches_before, difficulty):
        match_pile = MatchPile(matches_before, "triangle")
        player = ComputerPlayer("Machine", difficulty, match_pile)
        player.play_turn()
        matches_removed = matches_before - match_pile.get_remaining_matches()
        return matches_removed

    # A match is picked one time only.
    def verify_match(self, matches_before, matches_removed_expected,
                     difficulty):
        matches_removed = self.pick_match(matches_before, difficulty)
        self.assertEqual(matches_removed_expected, matches_removed)

    # A match is picked large number of times. Averages for each number of
    # matches picked is calculated, and the averages are compared with
    # theoretical expected values.
    def verify_match_statistical(self, matches_before, averages_expected,
                                 difficulty):

        repeats = 1000
        occurrences_realized = [0.0, 0.0, 0.0]

        for i in range(0, repeats):
            matches_removed = self.pick_match(matches_before, difficulty)
            occurrences_realized[matches_removed - 1] += 1.0

        averages_realized = [x / (1.0*repeats) for x in occurrences_realized]

        # (1.0 - allowed_deviation)*expected < realized
        # < (1.0 + allowed_deviation)*expected
        allowed_deviation = 0.25

        for i in range(0, 3):
            self.assertAlmostEqual(averages_expected[i], averages_realized[i],
                                   None, None,
                                   allowed_deviation * averages_expected[i])

    def test_constructors(self):
        match_pile = MatchPile(10, "triangle")

        player = ComputerPlayer("Machine", "easy", match_pile)
        self.assertEqual("computer", player.get_type())
        self.assertEqual("Machine", player.get_name())
        self.assertEqual("easy", player.get_difficulty())

        player = ComputerPlayer("Machine", "medium", match_pile)
        self.assertEqual("computer", player.get_type())
        self.assertEqual("Machine", player.get_name())
        self.assertEqual("medium", player.get_difficulty())

        player = ComputerPlayer("Machine", "hard", match_pile)
        self.assertEqual("computer", player.get_type())
        self.assertEqual("Machine", player.get_name())
        self.assertEqual("hard", player.get_difficulty())

    def test_hard_match_choosing(self):
        difficulty = "hard"

        self.verify_match(1, 1, difficulty)
        self.verify_match(2, 1, difficulty)
        self.verify_match(3, 2, difficulty)
        self.verify_match(4, 3, difficulty)
        self.verify_match(5, 1, difficulty)
        self.verify_match(6, 1, difficulty)
        self.verify_match(7, 2, difficulty)
        self.verify_match(8, 3, difficulty)
        self.verify_match(9, 1, difficulty)

    def test_easy_match_choosing(self):
        difficulty = "easy"

        self.verify_match_statistical(1, [1.00, 0.00, 0.00], difficulty)
        self.verify_match_statistical(2, [0.33, 0.67, 0.00], difficulty)
        self.verify_match_statistical(3, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(4, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(5, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(6, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(7, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(8, [0.33, 0.33, 0.33], difficulty)
        self.verify_match_statistical(9, [0.33, 0.33, 0.33], difficulty)

    def test_medium_match_choosing(self):
        difficulty = "medium"

        self.verify_match_statistical(1, [1.00, 0.00, 0.00], difficulty)
        self.verify_match_statistical(2, [0.67, 0.33, 0.00], difficulty)
        self.verify_match_statistical(3, [0.17, 0.67, 0.17], difficulty)
        self.verify_match_statistical(4, [0.17, 0.17, 0.67], difficulty)
        self.verify_match_statistical(5, [0.67, 0.17, 0.17], difficulty)
        self.verify_match_statistical(6, [0.67, 0.17, 0.17], difficulty)
        self.verify_match_statistical(7, [0.17, 0.67, 0.17], difficulty)
        self.verify_match_statistical(8, [0.17, 0.17, 0.67], difficulty)
        self.verify_match_statistical(9, [0.67, 0.17, 0.17], difficulty)


class TestHuman(unittest.TestCase):
    def verify_match(self, matches_before, matches_removed_expected, mock):
        match_pile = MatchPile(matches_before, "triangle")
        player = HumanPlayer("Man", match_pile)
        player._get_user_input = mock
        player.play_turn()
        matches_removed = matches_before - match_pile.get_remaining_matches()
        self.assertEqual(matches_removed_expected, matches_removed)

    def test_normal_match_picking_cases(self):
        mock = MagicMock()

        mock.return_value = "1"
        self.verify_match(10, 1, mock)

        mock.return_value = "2"
        self.verify_match(10, 2, mock)

        mock.return_value = "3"
        self.verify_match(10, 3, mock)

    def test_one_match_left(self):
        mock = MagicMock(side_effect=["3", "2", "1"])
        self.verify_match(1, 1, mock)
        self.assertEqual(3, mock.call_count)

    def test_two_matches_left(self):
        mock = MagicMock(side_effect=["3", "2", "1"])
        self.verify_match(2, 2, mock)
        self.assertEqual(2, mock.call_count)

    def test_invalid_user_input(self):
        mock = MagicMock(side_effect=["0", "4", "k", "1"])
        self.verify_match(10, 1, mock)
        self.assertEqual(4, mock.call_count)


if __name__ == '__main__':
    unittest.main()
