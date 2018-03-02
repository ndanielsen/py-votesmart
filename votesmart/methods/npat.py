"""
Npat methods that correspond to this API documentation page

Political Courage Test

Returns a candidates most recently filled out Political Courage Test.

http://api.votesmart.org/docs/Npat.html
"""

from .base import APIMethodBase

class Npat(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()
#     class Npat(object):
#         @staticmethod
#         def getNpat(candidateId):
#             params = {'candidateId':candidateId}
#             result = votesmart._apicall('Npat.getNpat', params)
#             return result['npat']
