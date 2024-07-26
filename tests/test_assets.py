import unittest
from src.masquer.utils.assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)


class TestAssets(unittest.TestCase):
    def test_header_data_is_dict_object(self):
        """HEADER_DATA is a dict object"""
        self.assertIsInstance(HEADER_DATA, dict)

    def test_header_data_has_content(self):
        """HEADER_DATA is not empty"""
        self.assertGreater(len(HEADER_DATA), 0)

    def test_header_data_keys_and_values_are_strings(self):
        """All keys and values of HEADER_DATA are str objects"""
        self.assertTrue(all(isinstance(x, str) for x in HEADER_DATA))
        self.assertTrue(all(isinstance(x, str) for x in HEADER_DATA.values()))

    def test_referers_is_list(self):
        """REFERERS is a list object"""
        self.assertIsInstance(REFERERS, list)

    def test_referers_has_content(self):
        """REFERERS is not empty"""
        self.assertGreater(len(REFERERS), 0)

    def test_referers_and_referer_weights_lengths(self):
        """REFERERS and REFERER_WEIGHTS have equal lengths"""
        self.assertEqual(len(REFERERS), len(REFERER_WEIGHTS))

    def test_referers_contains_strings(self):
        """All elements in REFERERS are str objects"""
        self.assertTrue(all(isinstance(x, str) for x in REFERERS))

    def test_referer_weights_is_list(self):
        """REFERER_WEIGHTS is a list object"""
        self.assertIsInstance(REFERER_WEIGHTS, list)

    def test_referer_weights_contains_floats(self):
        """All elements in REFERER_WEIGHTS are float objects"""
        self.assertTrue(all(isinstance(x, float) for x in REFERER_WEIGHTS))

    def test_referer_weights_contents_positive(self):
        """All elements in REFERER_WEIGHTS are positive values"""
        self.assertTrue(all(x > 0 for x in REFERER_WEIGHTS))

    def test_referer_weights_sorted_descending(self):
        """Values in REFERER_WEIGHTS are sorted in descending order"""
        self.assertEqual(REFERER_WEIGHTS, sorted(REFERER_WEIGHTS, reverse=True))

    def test_useragents_is_list(self):
        """USERAGENTS is a list object"""
        self.assertIsInstance(USERAGENTS, list)

    def test_useragents_has_content(self):
        """USERAGENTS is not empty"""
        self.assertGreater(len(USERAGENTS), 0)

    def test_useragents_and_useragent_weights_lengths(self):
        """USERAGENTS and USERAGENT_WEIGHTS have equal lengths"""
        self.assertEqual(len(USERAGENTS), len(USERAGENT_WEIGHTS))

    def test_useragents_contains_strings(self):
        """All elements in USERAGENTS are str objects"""
        self.assertTrue(all(isinstance(x, str) for x in USERAGENTS))

    def test_useragent_weights_is_list(self):
        """USERAGENT_WEIGHTS is a list object"""
        self.assertIsInstance(USERAGENT_WEIGHTS, list)

    def test_useragent_weights_contains_floats(self):
        """All elements in USERAGENT_WEIGHTS are float objects"""
        self.assertTrue(all(isinstance(x, float) for x in USERAGENT_WEIGHTS))

    def test_useragent_weights_contents_positive(self):
        """All elements in USERAGENT_WEIGHTS are positive values"""
        self.assertTrue(all(x > 0 for x in USERAGENT_WEIGHTS))

    def test_useragent_weights_sorted_descending(self):
        """Values in USERAGENT_WEIGHTS are sorted in descending order"""
        self.assertEqual(USERAGENT_WEIGHTS, sorted(USERAGENT_WEIGHTS, reverse=True))


if __name__ == "__main__":
    unittest.main()
