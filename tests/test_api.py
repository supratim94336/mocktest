import pytest
from src.api import Employee, GoGetter, DummyRequester


@pytest.mark.parametrize(
    "emp_1",
    [
        (Employee("Corey", "Schafer", 50000)),
    ]
)
def test_mock_api_call(mocker, emp_1):
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "Success"

    schedule = emp_1.monthly_schedule("May")
    mock_requests.assert_called_with("http://company.com/Schafer/May")
    assert schedule == "Success"


def test_success_get(mocker):
    """
    Show that the GoGetter can handle successful calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_success_get
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value = DummyRequester("waylonwalker", 200)
    # import requests
    # mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 200))
    assert "waylon" in go_getter.get()


def test_failed_get(mocker):
    """
    Show that the GoGetter can handle failed calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_failed_get
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value = DummyRequester("waylonwalker", 404)

    # import requests
    # mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 404))
    assert go_getter.get() is False
