"""
State methods that correspond to this API documentation page

http://api.votesmart.org/docs/State.html
"""


from .base import APIMethodBase
from .containers import VotesmartApiObject

class StateData(VotesmartApiObject):
    def __str__(self):
        return ' '.join((self.stateId, self.name))

class StateDetail(VotesmartApiObject):
    def __str__(self):
        return ' '.join((self.stateId, self.name))

class State(APIMethodBase):

    def getStateIDs(self):
        result = self.api.api_call('State.getStateIDs', {})
        return self.result_to_obj(StateData, result['stateList']['list']['state'])

    def getState(self, stateId):
        params = {'stateId' : stateId}
        result = self.api.api_call('State.getState', params)
        return StateDetail(result['state']['details'])
