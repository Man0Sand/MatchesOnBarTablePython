import unittest

from match_pile import Triangle
from match_pile import Square


class TestTriangle(unittest.TestCase):
    def _verify_coordinates(self, number_of_matches, width_expected,
                            height_expected, coordinates_expected):
        grid_coordinates = Triangle()
        width, height, coordinates = grid_coordinates.calculate(
            number_of_matches)
        self.assertEqual(width_expected, width)
        self.assertEqual(height_expected, height)
        self.assertEqual(coordinates_expected, coordinates)

    def test_0_matches(self):
        self._verify_coordinates(0, 0, 0, [])

    def test_1_match(self):
        self._verify_coordinates(1, 1, 1, [(0, 0)])

    def test_2_matches(self):
        self._verify_coordinates(2, 3, 1, [(0, 0), (2, 0)])

    def test_3_matches(self):
        self._verify_coordinates(3, 3, 2, [(1, 0),
                                           (0, 1), (2, 1)])

    def test_4_matches(self):
        self._verify_coordinates(4, 5, 2, [(2, 0),
                                           (0, 1), (2, 1), (4, 1)])

    def test_5_matches(self):
        self._verify_coordinates(5, 5, 2, [(1, 0), (3, 0),
                                           (0, 1), (2, 1), (4, 1)])

    def test_6_matches(self):
        self._verify_coordinates(6, 5, 3, [(2, 0),
                                           (1, 1), (3, 1),
                                           (0, 2), (2, 2), (4, 2)])


class TestSquare(unittest.TestCase):
    def _verify_coordinates(self, number_of_matches, width_expected,
                            height_expected, coordinates_expected):
        grid_coordinates = Square()
        width, height, coordinates = grid_coordinates.calculate(
            number_of_matches)
        self.assertEqual(width_expected, width)
        self.assertEqual(height_expected, height)
        self.assertEqual(coordinates_expected, coordinates)

    def test_0_matches(self):
        self._verify_coordinates(0, 0, 0, [])

    def test_1_match(self):
        self._verify_coordinates(1, 1, 1, [(0, 0)])

    def test_2_matches(self):
        self._verify_coordinates(2, 2, 1, [(0, 0), (1, 0)])

    def test_3_matches(self):
        self._verify_coordinates(3, 2, 2, [(0, 0),
                                           (0, 1), (1, 1)])

    def test_4_matches(self):
        self._verify_coordinates(4, 2, 2, [(0, 0), (1, 0),
                                           (0, 1), (1, 1)])

    def test_5_matches(self):
        self._verify_coordinates(5, 3, 2, [(0, 0), (1, 0),
                                           (0, 1), (1, 1), (2, 1)])

    def test_6_matches(self):
        self._verify_coordinates(6, 3, 2, [(0, 0), (1, 0), (2, 0),
                                           (0, 1), (1, 1), (2, 1)])

    def test_7_matches(self):
        self._verify_coordinates(7, 3, 3, [(0, 0),
                                           (0, 1), (1, 1), (2, 1),
                                           (0, 2), (1, 2), (2, 2)])

    def test_8_matches(self):
        self._verify_coordinates(8, 3, 3, [(0, 0), (1, 0),
                                           (0, 1), (1, 1), (2, 1),
                                           (0, 2), (1, 2), (2, 2)])

    def test_9_matches(self):
        self._verify_coordinates(9, 3, 3, [(0, 0), (1, 0), (2, 0),
                                           (0, 1), (1, 1), (2, 1),
                                           (0, 2), (1, 2), (2, 2)])

    def test_14_matches(self):
        self._verify_coordinates(14, 4, 4, [(0, 0), (1, 0),
                                            (0, 1), (1, 1), (2, 1), (3, 1),
                                            (0, 2), (1, 2), (2, 2), (3, 2),
                                            (0, 3), (1, 3), (2, 3), (3, 3)])

    def test_23_matches(self):
        self._verify_coordinates(23, 5, 5,
                                 [(0, 0), (1, 0), (2, 0),
                                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                                  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                                  (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                                  (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])


if __name__ == '__main__':
    unittest.main()
