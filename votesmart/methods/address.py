"""
Address methods that correspond to this API documentation page

http://api.votesmart.org/docs/Address.html
"""


from .base import APIMethodBase


class Address(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()

#         @staticmethod
#         def getCampaign(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('Address.getCampaign', params)
#             return _result_to_obj(AddressData, result['address']['office'])
#
#         @staticmethod
#         def getCampaignWebAddress(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('Address.getCampaignWebAddress', params)
#             return _result_to_obj(WebAddress, result['webaddress']['address'])
#
#         @staticmethod
#         def getCampaignByElection(electionId):
#             params = {'electionId': electionId}
#             result = votesmart._apicall('Address.getCampaignByElection', params)
#             return _result_to_obj(AddressData, result['address']['office'])
#
#         @staticmethod
#         def getOffice(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('Address.getOffice', params)
#             return _result_to_obj(AddressData, result['address']['office'])
#
#         @staticmethod
#         def getOfficeWebAddress(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('Address.getOfficeWebAddress', params)
#             return _result_to_obj(WebAddress, result['webaddress']['address'])
#
#         #@staticmethod
#         #def getOfficeByOfficeState(officeId, stateId=None):
#         #    params = {'officeId': officeId, 'stateId': stateId}
#         #    result = votesmart._apicall('Address.getOfficeByOfficeState', params)
#         #    return _result_to_obj(Address, result['address']['office'])
