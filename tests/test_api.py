import requests
import mock
import pytest
from pytest_mock import mocker

from votesmart.api import Votesmart

def test_sanity():
    assert 1 + 1 == 2

def test_init_api_no_key():
    with pytest.raises(ValueError):
        Votesmart()

def test_api_set_payload():
    vsmart = Votesmart(api_key="fake_key")
    params = vsmart._set_payload({"test": "okay"})

    assert params == {'key': vsmart.api_key, "o":"JSON", "test": "okay"}

def test_api__api_call(mocker):
    # mock the .json() function on requests
    json_mock = mock.Mock()
    json_mock.json.return_value = {'tests' : 'ok'}

    # patch requests in the function
    mocker.patch.object(requests, 'get')
    requests.get.return_value = json_mock

    vsmart = Votesmart(api_key="fake_key")

    response = vsmart._api_call('testFunction', {"param": 'one'})

    assert response == {'tests' : 'ok'}
