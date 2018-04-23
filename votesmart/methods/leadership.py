"""
Leadership methods that correspond to this API documentation page

http://api.votesmart.org/docs/Leadership.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class LeadershipPosition(VotesmartApiObject):
    def __str__(self):
        return self.name

class Leadership(APIMethodBase):

    def getPositions(self, stateId=None, officeId=None):
        params = {'stateId':stateId, 'officeId':officeId}
        result = self.api.api_call('Leadership.getPositions', params)
        return self.result_to_obj(LeadershipPosition, result['leadership']['position'])

    def getOfficials(self, leadershipId, stateId=None):
       params = {'leadershipId':leadershipId, 'stateId':stateId}
       result = self.api.api_call('Leadership.getOfficials', params)
       return result['leaders']['leader']
