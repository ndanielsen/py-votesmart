#     class Rating(object):
#         @staticmethod
#         def getCategories(stateId=None):
#             params = {'stateId':stateId}
#             result = votesmart._apicall('Rating.getCategories', params)
#             return _result_to_obj(Category, result['categories']['category'])
#
#         @staticmethod
#         def getSigList(categoryId, stateId=None):
#             params = {'categoryId':categoryId, 'stateId':stateId}
#             result = votesmart._apicall('Rating.getSigList', params)
#             return _result_to_obj(Sig, result['sigs']['sig'])
#
#         @staticmethod
#         def getSig(sigId):
#             params = {'sigId':sigId}
#             result = votesmart._apicall('Rating.getSig', params)
#             return SigDetail(result['sig'])
#
#         @staticmethod
#         def getCandidateRating(candidateId, sigId=None):
#             params = {'candidateId':candidateId, 'sigId':sigId}
#             result = votesmart._apicall('Rating.getCandidateRating', params)
#             return _result_to_obj(Rating, result['candidateRating']['rating'])
