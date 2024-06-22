import unittest
from split_code import split_items

class TestSplitItems(unittest.TestCase):

    def test_valid_split(self):
        items = [1, 2, 3, 4, 5, 6, 10]
        ratios = [0.5, 0.3, 0.2]
        expected_item_len = [3,2,1]
        result = split_items(items, ratios)
        result_items_len = [len(part) for part in result]
        self.assertEqual(len(result), 3)
        self.assertEqual(result_items_len, expected_item_len)

    def test_ratios_not_summing_to_one(self):
        items = [1, 2, 3, 4, 5, 6, 10]
        ratios = [0.5, 0.3, 0.3]
        result = split_items(items, ratios)
        self.assertEqual(result, "Error: Ratios must sum to 1")

    def test_empty_items(self):
        items = []
        ratios = [0.5, 0.5]
        result = split_items(items, ratios)
        self.assertEqual(result, "Error: Item list and ratio list should not be empty")

    def test_empty_ratios(self):
        items = [1, 2, 3, 4, 5]
        ratios = []
        result = split_items(items, ratios)
        self.assertEqual(result, "Error: Item list and ratio list should not be empty")

    def test_negative_ratios(self):
        items = [1, 2, 3, 4, 5]
        ratios = [0.5, -0.5]
        result = split_items(items, ratios)
        self.assertEqual(result, "Error: Ratios should be positive numbers")
    
    
if __name__ == '__main__':
    unittest.main()