import unittest
from src.masquer.utils.validate import validate_params


class TestValidateParams(unittest.TestCase):
    def test_calling_validate_params_with_valid_args_returns_true(self):
        """Calling validate_params() with valid args returns True"""
        self.assertTrue(validate_params(True, False, False))
        self.assertTrue(validate_params(True, True, False))
        self.assertTrue(validate_params(True, False, True))
        self.assertTrue(validate_params(True, True, True))
        self.assertTrue(validate_params(False, True, False))
        self.assertTrue(validate_params(False, True, True))
        self.assertTrue(validate_params(False, False, True))
        self.assertTrue(validate_params(False, False, False))

    def test_calling_validate_params_with_invalid_args_returns_false(self):
        """Calling validate_params() with invalid args returns False"""
        self.assertFalse(validate_params(0, True, True))
        self.assertFalse(validate_params(True, "string", True))
        self.assertFalse(validate_params(True, True, 0.0))
        self.assertFalse(validate_params([True], True, True))
        self.assertFalse(validate_params(True, (True,), True))
        self.assertFalse(validate_params(True, True, {True}))
        self.assertFalse(validate_params({"dict": True}, True, {True}))
        self.assertFalse(validate_params(None, None, None))
        self.assertFalse(validate_params(None, True, True))

    def test_calling_validate_params_with_missing_args_raises_type_error(self):
        """Calling validate_params() with missing args raises TypeError"""
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

    def test_calling_validate_params_with_surplus_args_raises_type_error(self):
        """Calling validate_params() with surplus args raises TypeError"""
        with self.assertRaises(TypeError):
            validate_params(True, True, True, True)
        with self.assertRaises(TypeError):
            validate_params(True, ua=True, rf=True, hd=True)


if __name__ == "__main__":
    unittest.main()
