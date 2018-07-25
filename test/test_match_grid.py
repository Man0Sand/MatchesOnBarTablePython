import unittest

from match_pile import Match
from match_pile import MatchGrid


class TestTriangleGrid(unittest.TestCase):
    def test_3_matches(self):
        matches = [Match() for i in range(3)]
        grid = MatchGrid("triangle", matches)
        self.assertEqual(3, grid.get_width())
        self.assertEqual(2, grid.get_height())

        # Elements originally without matches
        self.assertEqual(False, grid.has_match(0, 0))
        self.assertEqual(False, grid.has_match(2, 0))
        self.assertEqual(False, grid.has_match(1, 1))
        # Elements originally with matches
        self.assertEqual(True, grid.has_match(1, 0))
        self.assertEqual(True, grid.has_match(0, 1))
        self.assertEqual(True, grid.has_match(2, 1))

        matches[0].remove()
        # Elements originally without matches
        self.assertEqual(False, grid.has_match(0, 0))
        self.assertEqual(False, grid.has_match(2, 0))
        self.assertEqual(False, grid.has_match(1, 1))
        # Elements originally with matches
        self.assertEqual(False, grid.has_match(1, 0))
        self.assertEqual(True, grid.has_match(0, 1))
        self.assertEqual(True, grid.has_match(2, 1))

        matches[2].remove()
        # Elements originally without matches
        self.assertEqual(False, grid.has_match(0, 0))
        self.assertEqual(False, grid.has_match(2, 0))
        self.assertEqual(False, grid.has_match(1, 1))
        # Elements originally with matches
        self.assertEqual(False, grid.has_match(1, 0))
        self.assertEqual(True, grid.has_match(0, 1))
        self.assertEqual(False, grid.has_match(2, 1))

        matches[1].remove()
        # Elements originally without matches
        self.assertEqual(False, grid.has_match(0, 0))
        self.assertEqual(False, grid.has_match(2, 0))
        self.assertEqual(False, grid.has_match(1, 1))
        # Elements originally with matches
        self.assertEqual(False, grid.has_match(1, 0))
        self.assertEqual(False, grid.has_match(0, 1))
        self.assertEqual(False, grid.has_match(2, 1))


if __name__ == '__main__':
    unittest.main()
