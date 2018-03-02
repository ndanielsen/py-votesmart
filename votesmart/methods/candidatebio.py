"""
CandidateBio methods that correspond to this API documentation page

http://api.votesmart.org/docs/CandidateBio.html
"""


from .base import APIMethodBase

class CandidateBio(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()
#     class CandidateBio(object):
#         @staticmethod
#         def getBio(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('CandidateBio.getBio', params)
#             return Bio(result['bio'])
#
#         @staticmethod
#         def getAddlBio(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('CandidateBio.getAddlBio', params)
#             return _result_to_obj(AddlBio,
#                                   result['addlBio']['additional']['item'])
