
#     class Officials(object):
#         @staticmethod
#         def getStatewide(stateId=None):
#             params = {'stateId': stateId}
#             result = votesmart._apicall('Officials.getStatewide', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByOfficeState(officeId, stateId=None):
#             params = {'officeId':officeId, 'stateId': stateId}
#             result = votesmart._apicall('Officials.getByOfficeState', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByLastname(lastName):
#             params = {'lastName':lastName}
#             result = votesmart._apicall('Officials.getByLastname', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByLevenstein(lastName):
#             params = {'lastName':lastName}
#             result = votesmart._apicall('Officials.getByLevenstein', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByElection(electionId):
#             params = {'electionId':electionId}
#             result = votesmart._apicall('Officials.getByElection', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByDistrict(districtId):
#             params = {'districtId':districtId}
#             result = votesmart._apicall('Officials.getByDistrict', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
#
#         @staticmethod
#         def getByZip(zip5, zip4=None):
#             params = {'zip4': zip4, 'zip5': zip5}
#             result = votesmart._apicall('Officials.getByZip', params)
#             return _result_to_obj(Official, result['candidateList']['candidate'])
