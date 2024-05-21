import unittest
from src.masquerade.utils.validate import validate_params


class TestValidateParams(unittest.TestCase):
    def test_valid_params(self):
        """Test for valid parameters"""
        self.assertTrue(validate_params(True, False, False))
        self.assertTrue(validate_params(True, True, False))
        self.assertTrue(validate_params(True, False, True))
        self.assertTrue(validate_params(True, True, True))
        self.assertTrue(validate_params(False, True, False))
        self.assertTrue(validate_params(False, True, True))
        self.assertTrue(validate_params(False, False, True))
        self.assertTrue(validate_params(False, False, False))

    def test_invalid_params(self):
        """Test for invalid parameters"""
        self.assertFalse(validate_params(0, True, True))
        self.assertFalse(validate_params(True, "string", True))
        self.assertFalse(validate_params(True, True, 0.0))
        self.assertFalse(validate_params([True], True, True))
        self.assertFalse(validate_params(True, (True,), True))
        self.assertFalse(validate_params(True, True, {True}))
        self.assertFalse(validate_params({"dict": True}, True, {True}))
        self.assertFalse(validate_params(None, None, None))
        self.assertFalse(validate_params(None, True, True))

    def test_missing_params(self):
        """Test for missing parameters"""
        with self.assertRaises(TypeError):
            validate_params(True)
        with self.assertRaises(TypeError):
            validate_params(ua=True)
        with self.assertRaises(TypeError):
            validate_params(rf=True)
        with self.assertRaises(TypeError):
            validate_params(hd=True)
        with self.assertRaises(TypeError):
            validate_params(True, True)
        with self.assertRaises(TypeError):
            validate_params(ua=True, rf=True)
        with self.assertRaises(TypeError):
            validate_params(ua=True, hd=True)
        with self.assertRaises(TypeError):
            validate_params(rf=True, hd=True)

    def test_surplus_params(self):
        """Test for surplus parameters"""
        with self.assertRaises(TypeError):
            validate_params(True, True, True, True)
        with self.assertRaises(TypeError):
            validate_params(True, ua=True, rf=True, hd=True)


if __name__ == "__main__":
    unittest.main()
