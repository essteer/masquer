import unittest
from src.masquerade.utils.assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)


class TestAssets(unittest.TestCase):
    def test_header(self):
        """Test for header data"""
        self.assertIsInstance(HEADER_DATA, dict)
        self.assertGreater(len(HEADER_DATA), 0)
        self.assertTrue(all(isinstance(x, str) for x in HEADER_DATA))
        self.assertTrue(all(isinstance(x, str) for x in HEADER_DATA.values()))

    def test_referers(self):
        """Test for referer data"""
        self.assertIsInstance(REFERERS, list)
        self.assertGreater(len(REFERERS), 0)
        self.assertEqual(len(REFERERS), len(REFERER_WEIGHTS))
        self.assertTrue(all(isinstance(x, str) for x in REFERERS))

    def test_referer_weights(self):
        """Test for referer weights"""
        self.assertIsInstance(REFERER_WEIGHTS, list)
        self.assertTrue(all(isinstance(x, float) for x in REFERER_WEIGHTS))
        self.assertTrue(all(x > 0 for x in REFERER_WEIGHTS))
        self.assertEqual(REFERER_WEIGHTS, sorted(REFERER_WEIGHTS, reverse=True))

    def test_useragents(self):
        """Test for user-agent data"""
        self.assertIsInstance(USERAGENTS, list)
        self.assertGreater(len(USERAGENTS), 0)
        self.assertEqual(len(USERAGENTS), len(USERAGENT_WEIGHTS))
        self.assertTrue(all(isinstance(x, str) for x in USERAGENTS))

    def test_useragent_weights(self):
        """Test for user-agent weights"""
        self.assertIsInstance(USERAGENT_WEIGHTS, list)
        self.assertTrue(all(isinstance(x, float) for x in USERAGENT_WEIGHTS))
        self.assertTrue(all(x > 0 for x in USERAGENT_WEIGHTS))
        self.assertEqual(USERAGENT_WEIGHTS, sorted(USERAGENT_WEIGHTS, reverse=True))


if __name__ == "__main__":
    unittest.main()
