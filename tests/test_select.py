import unittest
from src.masquer.utils.assets import (
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from src.masquer.utils.select import select_data


class TestSelectData(unittest.TestCase):
    def test_calling_select_data_with_valid_args_returns_objects_of_expected_type(self):
        """Calling select_data() with valid args returns excepted object types"""
        samples = ["A", "list", "of", "strings"]
        weights = [0.25, 0.25, 0.25, 0.25]
        self.assertIsInstance(select_data(samples, weights), str)
        self.assertIsInstance(select_data(REFERERS, REFERER_WEIGHTS), str)
        self.assertIsInstance(select_data(USERAGENTS, USERAGENT_WEIGHTS), str)

    def test_calling_select_data_with_valid_args_returns_single_object(self):
        """Calling select_data() with valid args returns a single object"""
        samples = ["A", "list", "of", "strings"]
        weights = [0.25, 0.25, 0.25, 0.25]
        self.assertEqual(len([select_data(samples, weights)]), 1)
        self.assertEqual(len([select_data(REFERERS, REFERER_WEIGHTS)]), 1)
        self.assertEqual(len([select_data(USERAGENTS, USERAGENT_WEIGHTS)]), 1)

    def test_calling_select_data_with_valid_args_returns_selection_from_input_args(
        self,
    ):
        """Calling select_data() with valid args returns a selection from its input args"""
        samples = ["A", "list", "of", "strings"]
        weights = [0.25, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        self.assertIn(select_data(REFERERS, REFERER_WEIGHTS), REFERERS)
        self.assertIn(select_data(USERAGENTS, USERAGENT_WEIGHTS), USERAGENTS)

    def test_no_issues_arise_when_calling_select_data_with_weights_that_do_not_sum_to_1_(
        self,
    ):
        """Calling select_data() with weights that don't sum to 1 works OK"""
        samples = ["Another", "list", "of", "strings"]
        weights = [1, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        weights = [0.0, 0.25, 0.25, 0.25]
        self.assertIn(select_data(samples, weights), samples)
        weights = [30.0, 0.25, 10.25, 25.0]
        self.assertIn(select_data(samples, weights), samples)

    def test_calling_select_data_with_invalid_weight_types_raises_type_error(self):
        """Calling select_data() with invalid weights raises a TypeError"""
        samples = ["Yet", "another", "string", "list"]
        weights = ["0.25", 0.25, 0.25, 0.25]
        with self.assertRaises(TypeError):
            select_data(samples, weights)

    def test_calling_select_data_with_different_length_args_raises_value_error(self):
        """Calling select_data() with sample and weight lists of differing lengths raises a ValueError"""
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
