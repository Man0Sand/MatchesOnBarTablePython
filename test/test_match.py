import unittest
from match_pile import Match


class TestMatch(unittest.TestCase):
    def testRemoving(self):
        match = Match()
        self.assertEqual(True, match.isOnTable())
        match.remove()
        self.assertEqual(True, match.isRemoved())

    def testMarkingForRemoval(self):
        match = Match()
        match.toggleRemoval()
        self.assertEqual(True, match.isMarkedForRemoval())

    def testUnmarkingForRemoval(self):
        match = Match()
        match.toggleRemoval()
        match.toggleRemoval()
        self.assertEqual(False, match.isMarkedForRemoval())

    def testMarkingForRemovalAfterRemoving(self):
        match = Match()
        match.remove()
        match.toggleRemoval()
        self.assertEqual(False, match.isMarkedForRemoval())

    def testGettersForMatchOnTable(self):
        match = Match()
        self.assertEqual(True, match.isOnTable())
        self.assertEqual(False, match.isMarkedForRemoval())
        self.assertEqual(False, match.isRemoved())

    def testGettersForMatchMarkedForRemoval(self):
        match = Match()
        match.toggleRemoval()
        self.assertEqual(True, match.isOnTable())
        self.assertEqual(True, match.isMarkedForRemoval())
        self.assertEqual(False, match.isRemoved())

    def testGettersForRemovedMatch(self):
        match = Match()
        match.remove()
        self.assertEqual(False, match.isOnTable())
        self.assertEqual(False, match.isMarkedForRemoval())
        self.assertEqual(True, match.isRemoved())


if __name__ == '__main__':
    unittest.main()
