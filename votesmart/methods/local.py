"""
Local methods that correspond to this API documentation page

http://api.votesmart.org/docs/Local.html
"""

from .base import APIMethodBase

class Local(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()

#     class Local(object):
#         @staticmethod
#         def getCounties(stateId):
#             params = {'stateId': stateId}
#             result = votesmart._apicall('Local.getCounties', params)
#             return _result_to_obj(Locality, result['counties']['county'])
#
#         @staticmethod
#         def getCities(stateId):
#             params = {'stateId': stateId}
#             result = votesmart._apicall('Local.getCities', params)
#             return _result_to_obj(Locality, result['cities']['city'])
#
#         @staticmethod
#         def getOfficials(localId):
#             params = {'localId': localId}
#             result = votesmart._apicall('Local.getOfficials', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
