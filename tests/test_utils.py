import pytest
from votesmart import utils as uts
from votesmart.containers import VotesmartApiObject

# import _parse_api_response, VotesmartApiError

def test_sanity():
    assert 1 + 1 == 2

def test_parse_api_response():
    response = {"noerror": "here"}
    value = uts._parse_api_response(response)
    assert response == value

def test_parse_api_response_exception():
    with pytest.raises(uts.VotesmartApiError):
        response = {"error": {"errorMessage": "a message"}}
        value = uts._parse_api_response(response)

def test_result_to_obj():
    data = {}
    data['address'] = '123 address'
    data['phone'] = ['623-232-2321']
    data['notes'] = [" a note"]

    result = uts._result_to_obj(VotesmartApiObject, data)
    assert 1 == len(result)
    assert result[0].address == '123 address'
