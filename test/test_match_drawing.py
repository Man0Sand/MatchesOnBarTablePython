import unittest

from match_pile import MatchDrawing
from match_pile import Match

class TestTriangleDrawing(unittest.TestCase):
    def test_6_matches(self):
        matches = [Match() for i in range(6)]
        drawing = MatchDrawing("triangle", matches)

        drawing_expected = "  I  \n I I \nI I I\n"
        self.assertEqual(drawing_expected, drawing.draw())

        matches[0].remove()
        matches[1].remove()

        drawing_expected = "     \n   I \nI I I\n"
        self.assertEqual(drawing_expected, drawing.draw())

        matches[2].remove()
        drawing_expected = "     \n     \nI I I\n"
        self.assertEqual(drawing_expected, drawing.draw())

        matches[3].remove()
        matches[4].remove()
        matches[5].remove()
        drawing_expected = "     \n     \n     \n"
        self.assertEqual(drawing_expected, drawing.draw())

if __name__ == '__main__':
    unittest.main()
