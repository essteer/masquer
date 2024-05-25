import unittest
from src.masquer.utils.assets import (
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from src.masquer.utils.select import select_data


class TestSelectData(unittest.TestCase):
    def test_valid_input(self):
        """Test for valid input"""
        samples = ["A", "list", "of", "strings"]
        weights = [0.25, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        self.assertIsInstance(select_data(samples, weights), str)
        self.assertEqual(len([select_data(samples, weights)]), 1)
        self.assertIn(select_data(REFERERS, REFERER_WEIGHTS), REFERERS)
        self.assertIsInstance(select_data(REFERERS, REFERER_WEIGHTS), str)
        self.assertEqual(len([select_data(REFERERS, REFERER_WEIGHTS)]), 1)
        self.assertIn(select_data(USERAGENTS, USERAGENT_WEIGHTS), USERAGENTS)
        self.assertIsInstance(select_data(USERAGENTS, USERAGENT_WEIGHTS), str)
        self.assertEqual(len([select_data(USERAGENTS, USERAGENT_WEIGHTS)]), 1)

    def test_imbalanced_weights(self):
        """Test for weights that don't sum to 1"""
        samples = ["Another", "list", "of", "strings"]
        weights = [1, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        weights = [0.0, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        weights = [30.0, 0.25, 10.25, 25.0]
        self.assertIn(select_data(samples, weights), samples)

    def test_invalid_weights(self):
        """Test for invalid weights"""
        samples = ["Yet", "another", "string", "list"]
        weights = ["0.25", 0.25, 0.25, 0.25]
        with self.assertRaises(TypeError):
            select_data(samples, weights)

    def test_imbalanced_params(self):
        """Test for imbalanced parameter lists"""
        samples = ["A", "short", "list"]
        weights = [0.25, 0.25, 0.25, 0.25]
        with self.assertRaises(ValueError):
            select_data(samples, weights)
        samples = ["A", "much", "too", "long", "list"]
        weights = [0.25, 0.25, 0.25, 0.25]
        with self.assertRaises(ValueError):
            select_data(samples, weights)


if __name__ == "__main__":
    unittest.main()
