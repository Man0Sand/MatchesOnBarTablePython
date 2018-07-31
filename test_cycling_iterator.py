import unittest
from cycling_iterator import CyclingIterator


class TestCyclingIterator(unittest.TestCase):
    def test_everything(self):
        nums = [1, 2, 3]
        num_selector = CyclingIterator(nums)

        active_num = num_selector.advance()
        self.assertEqual(1, active_num)
        active_num = num_selector.advance()
        self.assertEqual(2, active_num)
        active_num = num_selector.advance()
        self.assertEqual(3, active_num)
        active_num = num_selector.advance()
        self.assertEqual(1, active_num)


if __name__ == '__main__':
    unittest.main()
