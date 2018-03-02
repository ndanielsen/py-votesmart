"""
Votes methods that correspond to this API documentation page

http://api.votesmart.org/docs/Votes.html
"""


from .base import APIMethodBase

class Votes(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()

#     class Votes(object):
#         @staticmethod
#         def getCategories(year, stateId=None):
#             params = {'year':year, 'stateId':stateId}
#             result = votesmart._apicall('Votes.getCategories', params)
#             return _result_to_obj(Category, result['categories']['category'])
#
#         @staticmethod
#         def getBill(billId):
#             params = {'billId':billId}
#             result = votesmart._apicall('Votes.getBill', params)
#             return BillDetail(result['bill'])
#
#         @staticmethod
#         def getBillAction(actionId):
#             params = {'actionId':actionId}
#             result = votesmart._apicall('Votes.getBillAction', params)
#             return BillActionDetail(result['action'])
#
#         @staticmethod
#         def getBillActionVotes(actionId):
#             params = {'actionId':actionId}
#             result = votesmart._apicall('Votes.getBillActionVotes', params)
#             return _result_to_obj(Vote, result['votes']['vote'])
#
#         @staticmethod
#         def getBillActionVoteByOfficial(actionId, candidateId):
#             params = {'actionId':actionId, 'candidateId':candidateId}
#             result = votesmart._apicall('Votes.getBillActionVoteByOfficial', params)
#             return Vote(result['votes']['vote'])
#
#         @staticmethod
#         def getByBillNumber(billNumber):
#             params = {'billNumber': billNumber}
#             result = votesmart._apicall('Votes.getByBillNumber', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByCategoryYearState(categoryId, year, stateId=None):
#             params = {'categoryId':categoryId, 'year':year, 'stateId':stateId}
#             result = votesmart._apicall('Votes.getBillsByCategoryYearState', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByYearState(year, stateId=None):
#             params = {'year':year, 'stateId':stateId}
#             result = votesmart._apicall('Votes.getBillsByYearState', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByOfficialYearOffice(candidateId, year, officeId=None):
#             params = {'candidateId':candidateId, 'year':year, 'officeId':officeId}
#             result = votesmart._apicall('Votes.getBillsByOfficialYearOffice', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByOfficial(candidateId, year, officeId=None, categoryId=None):
#             params = {'candidateId':candidateId, 'year':year, 'officeId':officeId, 'categoryId':categoryId}
#             result = votesmart._apicall('Votes.getBillsByOfficial', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByOfficialCategoryOffice(candidateId, categoryId, officeId=None):
#             params = {'candidateId':candidateId, 'categoryId':categoryId, 'officeId':officeId}
#             result = votesmart._apicall('Votes.getBillsByOfficialCategoryOffice', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsBySponsorYear(candidateId, year):
#             params = {'candidateId':candidateId, 'year':year}
#             result = votesmart._apicall('Votes.getBillsBySponsorYear', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsBySponsorCategory(candidateId, categoryId):
#             params = {'candidateId':candidateId, 'categoryId':categoryId}
#             result = votesmart._apicall('Votes.getBillsBySponsorCategory', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getBillsByStateRecent(stateId=None, amount=None):
#             params = {'stateId':stateId, 'amount':amount}
#             result = votesmart._apicall('Votes.getBillsByStateRecent', params)
#             return _result_to_obj(Bill, result['bills']['bill'])
#
#         @staticmethod
#         def getVetoes(candidateId):
#             params = {'candidateId': candidateId}
#             result = votesmart._apicall('Votes.getVetoes', params)
#             return _result_to_obj(Veto, result['vetoes']['veto'])
