import unittest
from unittest.mock import patch
from src.masquer.utils.assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from src.masquer.utils.response import get_response


class TestGetResponse(unittest.TestCase):
    def test_get_response_header_data_output(self):
        """get_response() returns expected HEADER_DATA output"""
        self.assertEqual(get_response(False, False, True), HEADER_DATA)
        self.assertEqual(get_response(False, False, False), dict())

    def test_get_response_referer_output(self):
        """get_response() returns expected REFERERS data across different args combinations"""
        for _ in range(20):
            output = get_response(False, True, False)
            self.assertTrue(any([x in output.values() for x in REFERERS]))
        for _ in range(20):
            output = get_response(True, True, False)
            self.assertTrue(any([x in output.values() for x in REFERERS]))
        for _ in range(20):
            output = get_response(True, True, True)
            self.assertTrue(any([x in output.values() for x in REFERERS]))
        for _ in range(20):
            output = get_response(False, True, True)
            self.assertTrue(any([x in output.values() for x in REFERERS]))

    def test_get_response_useragents_output(self):
        """get_response() returns expected USERAGENTS data across different args combinations"""
        for _ in range(20):
            output = get_response(True, False, False)
            self.assertTrue(any([x in output.values() for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, True, False)
            self.assertTrue(any([x in output.values() for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, False, True)
            self.assertTrue(any([x in output.values() for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, True, True)
            self.assertTrue(any([x in output.values() for x in USERAGENTS]))

    @patch("random.choices")
    def test_get_response_referer_args(self, mock_choices):
        """get_response() makes a single function call with REFERERS and REFERER_WEIGHTS"""
        mock_choices.return_value = ["referer1"]
        get_response(False, True, False)
        mock_choices.assert_called_once_with(REFERERS, weights=REFERER_WEIGHTS, k=1)

    @patch("random.choices")
    def test_get_response_useragent_args(self, mock_choices):
        """get_response() makes a single function call with USERAGENTS and USERAGENT_WEIGHTS"""
        mock_choices.return_value = ["useragent1"]
        get_response(True, False, False)
        mock_choices.assert_called_once_with(USERAGENTS, weights=USERAGENT_WEIGHTS, k=1)


if __name__ == "__main__":
    unittest.main()
