"""
Committee methods that correspond to this API documentation page

http://api.votesmart.org/docs/Committee.html
"""

from .base import APIMethodBase

class Committee(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()
#     class Committee(object):
#         @staticmethod
#         def getTypes():
#             result = votesmart._apicall('Committee.getTypes', {})
#             return _result_to_obj(CommitteeType, result['committeeTypes']['type'])
#
#         @staticmethod
#         def getCommitteesByTypeState(typeId=None, stateId=None):
#             params = {'typeId':typeId, 'stateId':stateId}
#             result = votesmart._apicall('Committee.getCommitteesByTypeState', params)
#             return _result_to_obj(Committee, result['committees']['committee'])
#
#         @staticmethod
#         def getCommittee(committeeId):
#             params = {'committeeId' : committeeId}
#             result = votesmart._apicall('Committee.getCommittee', params)
#             return CommitteeDetail(result['committee'])
#
#         @staticmethod
#         def getCommitteeMembers(committeeId):
#             params = {'committeeId' : committeeId}
#             result = votesmart._apicall('Committee.getCommitteeMembers', params)
#             return _result_to_obj(CommitteeMember, result['committeeMembers']['member'])
