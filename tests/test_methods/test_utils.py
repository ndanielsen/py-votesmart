import pytest
from votesmart.methods import utils as uts
from votesmart.methods.containers import VotesmartApiObject

# import _parse_api_response, VotesmartApiError

def test_sanity():
    assert 1 + 1 == 2

def test_parse_api_response():
    response = {"noerror": "here"}
    value = uts.parse_api_response(response)
    assert response == value

def test_parse_api_response_exception():
    with pytest.raises(uts.VotesmartApiError):
        response = {"error": {"errorMessage": "a message"}}
        value = uts.parse_api_response(response)
