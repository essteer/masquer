import unittest
from unittest.mock import patch
from src.masquerade.utils.assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from src.masquerade.utils.response import get_response


class TestGetResponse(unittest.TestCase):
    def test_header_data(self):
        """Test for valid header output"""
        output = get_response(False, False, True).replace('"', "'")
        self.assertEqual(output, str(HEADER_DATA))
        self.assertEqual(get_response(False, False, False), str(dict()))

    def test_referers(self):
        """Test for valid referer output"""
        for _ in range(20):
            output = get_response(False, True, False)
            self.assertTrue(any([x in output for x in REFERERS]))
        for _ in range(20):
            output = get_response(True, True, False)
            self.assertTrue(any([x in output for x in REFERERS]))
        for _ in range(20):
            output = get_response(True, True, True)
            self.assertTrue(any([x in output for x in REFERERS]))
        for _ in range(20):
            output = get_response(False, True, True)
            self.assertTrue(any([x in output for x in REFERERS]))

    def test_useragents(self):
        """Test for valid user-agent output"""
        for _ in range(20):
            output = get_response(True, False, False)
            self.assertTrue(any([x in output for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, True, False)
            self.assertTrue(any([x in output for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, False, True)
            self.assertTrue(any([x in output for x in USERAGENTS]))
        for _ in range(20):
            output = get_response(True, True, True)
            self.assertTrue(any([x in output for x in USERAGENTS]))

    @patch("random.choices")
    def test_referer_weight_selection(self, mock_choices):
        """Test if referer selection uses weights from REFERER_WEIGHTS"""
        mock_choices.return_value = ["referer1"]
        get_response(False, True, False)
        mock_choices.assert_called_once_with(REFERERS, weights=REFERER_WEIGHTS, k=1)

    @patch("random.choices")
    def test_useragent_weight_selection(self, mock_choices):
        """Test if user-agent selection uses weights from USERAGENT_WEIGHTS"""
        mock_choices.return_value = ["useragent1"]
        get_response(True, False, False)
        mock_choices.assert_called_once_with(USERAGENTS, weights=USERAGENT_WEIGHTS, k=1)


if __name__ == "__main__":
    unittest.main()
