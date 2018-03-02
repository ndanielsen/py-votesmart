"""
District methods that correspond to this API documentation page

http://api.votesmart.org/docs/District.html
"""


from .base import APIMethodBase

class District(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()

#     class District(object):
#         @staticmethod
#         def getByOfficeState(officeId, stateId, districtName=None):
#             params = {'officeId':officeId, 'stateId': stateId, 'districtName': districtName}
#             result = votesmart._apicall('District.getByOfficeState', params)
#             return _result_to_obj(District, result['districtList']['district'])
#
#         @staticmethod
#         def getByZip(zip5, zip4=None):
#             params = {'zip5': zip5, 'zip4': zip4}
#             result = votesmart._apicall('District.getByZip', params)
#             return _result_to_obj(District, result['districtList']['district'])
