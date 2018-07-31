import unittest
from unittest.mock import MagicMock
from match_pile import MatchPile


class TestTrianglePile(unittest.TestCase):
    def test_removing(self):
        match_pile = MatchPile(6, "triangle")
        match_pile._output_to_screen = MagicMock()

        self.assertEqual(6, match_pile.get_remaining_matches())

        match_pile.print_matches()
        pile_expected = "  I  \n I I \nI I I\n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(1)
        self.assertEqual(5, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n I I \nI I I\n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(2)
        self.assertEqual(3, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n     \nI I I\n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(-2)
        self.assertEqual(3, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n     \nI I I\n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(4)
        self.assertEqual(3, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n     \nI I I\n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(3)
        self.assertEqual(0, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n     \n     \n"
        match_pile._output_to_screen.assert_called_with(pile_expected)

        match_pile.remove_matches(1)
        self.assertEqual(0, match_pile.get_remaining_matches())
        match_pile.print_matches()
        pile_expected = "     \n     \n     \n"
        match_pile._output_to_screen.assert_called_with(pile_expected)


if __name__ == '__main__':
    unittest.main()
