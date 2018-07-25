import unittest
from match import Match


class TestMatch(unittest.TestCase):
    def test_everything(self):
        match = Match()
        self.assertEqual(False, match.is_removed())
        match.remove()
        self.assertEqual(True, match.is_removed())
        match.remove()
        self.assertEqual(True, match.is_removed())


if __name__ == '__main__':
    unittest.main()
