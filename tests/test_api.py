import requests
import mock
import pytest
from pytest_mock import mocker

from votesmart.api import VoteSmartAPI

def test_sanity():
    assert 1 + 1 == 2

def test_init_api_no_key():
    with pytest.raises(ValueError):
        VoteSmartAPI()

def test_api_set_payload():
    vsmart = VoteSmartAPI(api_key="fake_key")
    params = vsmart._set_payload({"test": "okay"})

    assert params == {'key': vsmart.api_key, "o":"JSON", "test": "okay"}

def test_api_api_call(mocker):
    # mock the .json() function on requests
    json_mock = mock.Mock()
    json_mock.json.return_value = {'tests' : 'ok'}

    # patch requests in the function
    mocker.patch.object(requests, 'get')
    requests.get.return_value = json_mock

    vsmart = VoteSmartAPI(api_key="fake_key")

    response = vsmart.api_call('testFunction', {"param": 'one'})

    assert response == {'tests' : 'ok'}
