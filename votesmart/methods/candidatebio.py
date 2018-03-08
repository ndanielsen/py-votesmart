"""
CandidateBio methods that correspond to this API documentation page

http://api.votesmart.org/docs/CandidateBio.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class Bio(VotesmartApiObject):
    def __init__(self, d):
        self.__dict__.update(d['candidate'])

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)

class AddlBio(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.name, self.data))


class CandidateBio(APIMethodBase):
    def getBio(self, candidateId):
        params = {'candidateId': candidateId}
        result = self.api.api_call('CandidateBio.getBio', params)
        return Bio(result['bio'])

    def getDetailedBio(self, candidateId):
        params = {'candidateId': candidateId}
        result = self.api.api_call('CandidateBio.getDetailedBio', params)
        return Bio(result['bio'])

    def getAddlBio(self, candidateId):
        params = {'candidateId': candidateId}
        result = self.api.api_call('CandidateBio.getAddlBio', params)
        return self.result_to_obj(AddlBio,
                              result['addlBio']['additional']['item'])
