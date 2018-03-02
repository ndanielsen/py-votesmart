"""
District methods that correspond to this API documentation page

http://api.votesmart.org/docs/District.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class DistrictData(VotesmartApiObject):
    def __str__(self):
        return self.name

class District(APIMethodBase):

    def getByOfficeState(self, officeId, stateId, districtName=None):
        params = {'officeId':officeId, 'stateId': stateId, 'districtName': districtName}
        result = self.api.api_call('District.getByOfficeState', params)
        return self.result_to_obj(DistrictData, result['districtList']['district'])

    def getByZip(self, zip5, zip4=None):
        params = {'zip5': zip5, 'zip4': zip4}
        result = self.api.api_call('District.getByZip', params)
        return self.result_to_obj(DistrictData, result['districtList']['district'])
