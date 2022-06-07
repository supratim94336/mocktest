import unittest
import requests
import pytest
from src.side_effects import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch
from unittest.mock import Mock


@patch('src.side_effects.requests')
def test_get_holidays_timeout_patch_decorator(mock_requests):
    mock_requests.get.side_effect = Timeout
    with pytest.raises(Timeout):
        get_holidays()
        mock_requests.get.assert_called_once()


def test_get_holidays_timeout_patch_object():
    with patch('src.side_effects.requests') as mock_requests:
        mock_requests.get.side_effect = Timeout
        with pytest.raises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


class TestCalendar(unittest.TestCase):
    @patch('src.side_effects.requests')
    def test_get_holidays_timeout_class(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

    @patch('src.side_effects.requests')
    def test_get_holidays_retry(self, mock_requests):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of .get() (!!order is important)
        mock_requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'
        # Finally, assert .get() was called twice
        assert mock_requests.get.call_count == 2
