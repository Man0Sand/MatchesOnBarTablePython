import unittest
from match_pile import MatchPile


class TestTrianglePile(unittest.TestCase):
    def test_removing(self):
        match_pile = MatchPile(6, "triangle")
        self.assertEqual(6, match_pile.get_remaining_matches())

        match_pile.remove_matches(1)
        self.assertEqual(5, match_pile.get_remaining_matches())

        match_pile.remove_matches(2)
        self.assertEqual(3, match_pile.get_remaining_matches())

        match_pile.remove_matches(-2)
        self.assertEqual(3, match_pile.get_remaining_matches())

        match_pile.remove_matches(4)
        self.assertEqual(3, match_pile.get_remaining_matches())

        match_pile.remove_matches(3)
        self.assertEqual(0, match_pile.get_remaining_matches())

        match_pile.remove_matches(1)
        self.assertEqual(0, match_pile.get_remaining_matches())


if __name__ == '__main__':
    unittest.main()
