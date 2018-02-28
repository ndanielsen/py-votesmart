import requests

from .utils import _parse_api_response
from .exceptions import VotesmartApiError

class VoteSmartAPI:
    def __init__(self, api_key=None):
        if api_key is None:
            raise ValueError('A Votesmart api_key is required')
        self.api_key = api_key

    def _api_call(self, function, params):
        request_str = "http://api.votesmart.org/{function}".format(function=function)
        payload = self._set_payload(params)
        response = requests.get(request_str, params=payload)
        return _parse_api_response(response.json())

    def _set_payload(self, params):
        params = params.copy()
        params.update({'key': self.api_key, "o":"JSON"})
        return params
