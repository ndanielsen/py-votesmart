"""
Leadership methods that correspond to this API documentation page

http://api.votesmart.org/docs/Leadership.html
"""

from .base import APIMethodBase

class Leadership(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()
#     class Leadership(object):
#         @staticmethod
#         def getPositions(stateId=None, officeId=None):
#             params = {'stateId':stateId, 'officeId':officeId}
#             result = votesmart._apicall('Leadership.getPositions', params)
#             return _result_to_obj(LeadershipPosition, result['leadership']['position'])
#
#         @staticmethod
#         def getOfficials(leadershipId, stateId=None):
#            params = {'leadershipId':leadershipId, 'stateId':stateId}
#            result = votesmart._apicall('Leadership.getOfficials', params)
#            return result['leaders']['leader']
