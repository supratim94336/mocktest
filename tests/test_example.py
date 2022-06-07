from datetime import datetime
import pytest

from src.example import process_data
from src.example import get_time_of_day
from src.example import add


def test_add():
    # Arrange
    a = 2
    b = 5
    expected = 7

    # Act
    output = add(a, b)

    # Assert
    assert output == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 5, 15),
        (-1, 1, 0),
        (-1, -1, -2)
    ]
)
def test_add_params(a, b, expected):
    assert add(a, b) == expected


def test_process_data(mocker):
    mocker.patch("src.example.load_data", return_value={"key1": "val1", "key2": "val2"})
    assert process_data() == "val1"


def test_get_time_of_day(mocker):
    mock_now = mocker.patch("src.example.datetime")
    mock_now.now.return_value = datetime(2016, 5, 20, 14, 10, 0)
    assert get_time_of_day() == "Afternoon"


@pytest.mark.parametrize(
    "datetime_obj, expect",
    [
        (datetime(2016, 5, 20, 0, 0, 0), "Night"),
        (datetime(2016, 5, 20, 1, 10, 0), "Night"),
        (datetime(2016, 5, 20, 6, 10, 0), "Morning"),
        (datetime(2016, 5, 20, 12, 0, 0), "Afternoon"),
        (datetime(2016, 5, 20, 14, 10, 0), "Afternoon"),
        (datetime(2016, 5, 20, 18, 0, 0), "Evening"),
        (datetime(2016, 5, 20, 19, 10, 0), "Evening"),
    ],
)
def test_get_time_of_day_params(datetime_obj, expect, mocker):
    mock_now = mocker.patch("src.example.datetime")
    mock_now.now.return_value = datetime_obj
    assert get_time_of_day() == expect
