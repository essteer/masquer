import unittest
from src.masquer.app import masq


class TestMasq(unittest.TestCase):
    def test_all_blank_inputs(self):
        """Test with all blank inputs"""
        self.assertIsInstance(masq(), str)
        self.assertIsInstance(masq(ua=False, rf=False, hd=False), str)

    def test_valid_boolean_input(self):
        """Test with valid boolean inputs"""
        self.assertIsInstance(masq(ua=True, rf=False, hd=False), str)
        self.assertIsInstance(masq(ua=True, rf=True, hd=False), str)
        self.assertIsInstance(masq(ua=True, rf=True, hd=True), str)
        self.assertIsInstance(masq(ua=False, rf=True, hd=False), str)
        self.assertIsInstance(masq(ua=False, rf=True, hd=True), str)
        self.assertIsInstance(masq(ua=False, rf=False, hd=True), str)
        self.assertIsInstance(masq(ua=True, rf=False, hd=True), str)
        self.assertIsInstance(masq(ua=False, rf=False, hd=False), str)
        self.assertIsInstance(masq(ua=True), str)
        self.assertIsInstance(masq(ua=False), str)
        self.assertIsInstance(masq(rf=True), str)
        self.assertIsInstance(masq(rf=False), str)
        self.assertIsInstance(masq(hd=True), str)
        self.assertIsInstance(masq(hd=False), str)

    def test_non_boolean_input(self):
        """Test for non boolean input"""
        error_msg = "Error: ua|rf|hd must be blank or boolean"
        self.assertEqual(masq(0), error_msg)
        self.assertEqual(masq(ua=0), error_msg)
        self.assertEqual(masq(rf=0), error_msg)
        self.assertEqual(masq(hd=0), error_msg)
        self.assertEqual(masq("True"), error_msg)
        self.assertEqual(masq(None), error_msg)
        self.assertEqual(masq(ua=True, rf=True, hd=0), error_msg)

    def test_surplus_params(self):
        """Test for surplus parameters"""
        with self.assertRaises(TypeError):
            masq(True, True, True, True)
        with self.assertRaises(TypeError):
            masq(True, ua=True, rf=True, hd=True)


if __name__ == "__main__":
    unittest.main()
