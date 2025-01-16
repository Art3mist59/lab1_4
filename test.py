
import unittest
from lib import count_common_elements

class TestCountCommonElements(unittest.TestCase):

    def test_no_lists(self):
        self.assertEqual(count_common_elements(), 0)

    def test_no_common_elements(self):
        self.assertEqual(count_common_elements([1, 2, 3], [4, 5, 6]), 0)

    def test_some_common_elements(self):
        self.assertEqual(count_common_elements([1, 2, 3], [2, 3, 4], [3, 5]), 1)

    def test_all_common_elements(self):
        self.assertEqual(count_common_elements([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_empty_lists(self):
        self.assertEqual(count_common_elements([], []), 0)
        self.assertEqual(count_common_elements([1, 2, 3], []), 0)

    def test_identical_lists(self):
        self.assertEqual(count_common_elements([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()