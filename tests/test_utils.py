import pytest
from votesmart.utils import _parse_api_response, VotesmartApiError

def test_sanity():
    assert 1 + 1 == 2

def test_parse_api_response():
    response = {"noerror": "here"}
    value = _parse_api_response(response)
    assert response == value

def test_parse_api_response_exception():
    with pytest.raises(VotesmartApiError):
        response = {"error": {"errorMessage": "a message"}}
        value = _parse_api_response(response)
