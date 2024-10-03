import pytest
import urllib.request
from unittest.mock import patch, MagicMock

# Import fetchincidents from your actual module
from project0 import fetchincidents

@patch('urllib.request.urlopen')
def test_fetch_incidents_with_headers(mock_urlopen):
    # Set up the mock response
    mock_response = MagicMock()
    mock_response.read.return_value = b"Ishtmeet"

    # Assign the mock response to urlopen
    mock_urlopen.return_value = mock_response

    # URL to be used in the test
    test_url = "http://example.com/test"

    # Call the function
    result = fetchincidents.fetchIncidents(test_url)

    request_args, _ = mock_urlopen.call_args
    request = request_args[0]

    # Ensure that urlopen was called correctly
    assert isinstance(request, urllib.request.Request)
    assert request.full_url == test_url

    # Assert the function's result is what we expect
    assert result == b"Ishtmeet"
