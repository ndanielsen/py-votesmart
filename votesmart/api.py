import os

import requests
import six

from .methods.utils import parse_api_response

from .exceptions import VotesmartApiError
from . import methods

class VoteSmartAPI:
    def __init__(self, api_key=None):
        if api_key is None:
            raise ValueError('A Votesmart api_key is required')
        self.api_key = api_key

    def api_call(self, function, params):
        request_str = "http://api.votesmart.org/{function}".format(function=function)
        payload = self._set_payload(params)
        response = requests.get(request_str, params=payload)
        try:
            parsed_data = parse_api_response(response.json())
            return parsed_data
        except ValueError:
            raise VotesmartApiError('Problem with API Response')


    def _set_payload(self, params):
        params = params.copy()
        params.update({'key': self.api_key, "o":"JSON"})
        return params

    @property
    def Address(self):
        return methods.Address(self)

    @property
    def CandidateBio(self):
        return methods.CandidateBio(self)

    @property
    def Candidates(self):
        return methods.Candidates(self)

    @property
    def Committee(self):
        return methods.Committee(self)

    @property
    def District(self):
        return methods.District(self)

    @property
    def Election(self):
        return methods.Election(self)

    @property
    def Leadership(self):
        return methods.Leadership(self)

    @property
    def Local(self):
        return methods.Local(self)

    @property
    def Measure(self):
        return methods.Measure(self)

    @property
    def Npat(self):
        return methods.Npat(self)

    @property
    def Office(self):
        return methods.Office(self)

    @property
    def Officials(self):
        return methods.Officials(self)

    @property
    def State(self):
        return methods.State(self)

    @property
    def Rating(self):
        return methods.Rating(self)

    @property
    def Votes(self):
        return methods.Votes(self)
