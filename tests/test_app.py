import unittest
from src.masquer.app import masq


class TestMasq(unittest.TestCase):
    def test_calling_masq_without_args_returns_dict_object(self):
        """Calling masq() without args still returns a dict object"""
        self.assertIsInstance(masq(), dict)
        self.assertIsInstance(masq(ua=False, rf=False, hd=False), dict)

    def test_calling_masq_with_valid_boolean_input_args_return_dict_objects(self):
        """Calling masq() with valid args combinations returns a dict object"""
        self.assertIsInstance(masq(ua=True, rf=False, hd=False), dict)
        self.assertIsInstance(masq(ua=True, rf=True, hd=False), dict)
        self.assertIsInstance(masq(ua=True, rf=True, hd=True), dict)
        self.assertIsInstance(masq(ua=False, rf=True, hd=False), dict)
        self.assertIsInstance(masq(ua=False, rf=True, hd=True), dict)
        self.assertIsInstance(masq(ua=False, rf=False, hd=True), dict)
        self.assertIsInstance(masq(ua=True, rf=False, hd=True), dict)
        self.assertIsInstance(masq(ua=False, rf=False, hd=False), dict)
        self.assertIsInstance(masq(ua=True), dict)
        self.assertIsInstance(masq(ua=False), dict)
        self.assertIsInstance(masq(rf=True), dict)
        self.assertIsInstance(masq(rf=False), dict)
        self.assertIsInstance(masq(hd=True), dict)
        self.assertIsInstance(masq(hd=False), dict)

    def test_calling_masq_with_invalid_args_returns_error_message(self):
        """Calling masq() with invalid args returns an error message"""
        error_msg = "Error: ua|rf|hd must be blank or boolean"
        self.assertEqual(masq(0), error_msg)
        self.assertEqual(masq(ua=0), error_msg)
        self.assertEqual(masq(rf=0), error_msg)
        self.assertEqual(masq(hd=0), error_msg)
        self.assertEqual(masq("True"), error_msg)
        self.assertEqual(masq(None), error_msg)
        self.assertEqual(masq(ua=True, rf=True, hd=0), error_msg)

    def test_calling_masq_with_surplus_args_raises_type_error(self):
        """Calling masq() with surplus args raises a TypeError"""
        with self.assertRaises(TypeError):
            masq(True, True, True, True)
        with self.assertRaises(TypeError):
            masq(True, ua=True, rf=True, hd=True)


if __name__ == "__main__":
    unittest.main()
