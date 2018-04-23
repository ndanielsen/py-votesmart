"""
Local methods that correspond to this API documentation page

http://api.votesmart.org/docs/Local.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class Locality(VotesmartApiObject):
    def __str__(self):
        return self.name

class Official(VotesmartApiObject):
    def __str__(self):
        return ' '.join((self.title, self.firstName, self.lastName))

class Local(APIMethodBase):

    def getCounties(self, stateId):
        params = {'stateId': stateId}
        result = self.api.api_call('Local.getCounties', params)
        return self.result_to_obj(Locality, result['counties']['county'])

    def getCities(self, stateId):
        params = {'stateId': stateId}
        result = self.api.api_call('Local.getCities', params)
        return self.result_to_obj(Locality, result['cities']['city'])

    def getOfficials(self, localId):
        params = {'localId': localId}
        result = self.api.api_call('Local.getOfficials', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])
