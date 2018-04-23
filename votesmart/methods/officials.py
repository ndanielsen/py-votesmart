"""
Officials methods that correspond to this API documentation page

http://api.votesmart.org/docs/Officials.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class Official(VotesmartApiObject):
    def __str__(self):
        return ' '.join((self.title, self.firstName, self.lastName))

class OfficeType(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.officeTypeId, self.name))


class Officials(APIMethodBase):

    def getTypes(self):
        result = self.api.api_call('Office.getTypes', {})
        return self.result_to_obj(OfficeType, result['officeTypes']['type'])

    def getStatewide(self, stateId=None):
        params = {'stateId': stateId}
        result = self.api.api_call('Officials.getStatewide', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])

    def getByOfficeState(self, officeId, stateId=None):
        params = {'officeId':officeId, 'stateId': stateId}
        result = self.api.api_call('Officials.getByOfficeState', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])

    def getByLastname(self, lastName):
        params = {'lastName':lastName}
        result = self.api.api_call('Officials.getByLastname', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])

    def getByLevenstein(self, lastName):
        params = {'lastName':lastName}
        result = self.api.api_call('Officials.getByLevenstein', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])

    def getByDistrict(self, districtId):
        params = {'districtId':districtId}
        result = self.api.api_call('Officials.getByDistrict', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])

    def getByZip(self, zip5, zip4=None):
        params = {'zip4': zip4, 'zip5': zip5}
        result = self.api.api_call('Officials.getByZip', params)
        return self.result_to_obj(Official, result['candidateList']['candidate'])
