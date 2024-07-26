import unittest
from src.masquer.utils.validate import validate_args


class TestValidateParams(unittest.TestCase):
    def test_validate_args_with_valid_args(self):
        """Calling validate_args() with valid args returns True"""
        self.assertTrue(validate_args(True, False, False))
        self.assertTrue(validate_args(True, True, False))
        self.assertTrue(validate_args(True, False, True))
        self.assertTrue(validate_args(True, True, True))
        self.assertTrue(validate_args(False, True, False))
        self.assertTrue(validate_args(False, True, True))
        self.assertTrue(validate_args(False, False, True))
        self.assertTrue(validate_args(False, False, False))

    def test_validate_args_with_invalid_args(self):
        """Calling validate_args() with invalid args returns False"""
        self.assertFalse(validate_args(0, True, True))
        self.assertFalse(validate_args(True, "string", True))
        self.assertFalse(validate_args(True, True, 0.0))
        self.assertFalse(validate_args([True], True, True))
        self.assertFalse(validate_args(True, (True,), True))
        self.assertFalse(validate_args(True, True, {True}))
        self.assertFalse(validate_args({"dict": True}, True, {True}))
        self.assertFalse(validate_args(None, None, None))
        self.assertFalse(validate_args(None, True, True))

    def test_validate_args_with_missing_args(self):
        """Calling validate_args() with missing args raises TypeError"""
        with self.assertRaises(TypeError):
            validate_args(True)
        with self.assertRaises(TypeError):
            validate_args(ua=True)
        with self.assertRaises(TypeError):
            validate_args(rf=True)
        with self.assertRaises(TypeError):
            validate_args(hd=True)
        with self.assertRaises(TypeError):
            validate_args(True, True)
        with self.assertRaises(TypeError):
            validate_args(ua=True, rf=True)
        with self.assertRaises(TypeError):
            validate_args(ua=True, hd=True)
        with self.assertRaises(TypeError):
            validate_args(rf=True, hd=True)

    def test_validate_args_with_surplus_args(self):
        """Calling validate_args() with surplus args raises TypeError"""
        with self.assertRaises(TypeError):
            validate_args(True, True, True, True)
        with self.assertRaises(TypeError):
            validate_args(True, ua=True, rf=True, hd=True)


if __name__ == "__main__":
    unittest.main()
