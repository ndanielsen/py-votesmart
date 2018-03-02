"""
Office methods that correspond to this API documentation page

http://api.votesmart.org/docs/Office.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject, Candidate
from .utils import result_to_obj

class OfficeData(VotesmartApiObject):
    def __str__(self):
        return self.name

class OfficeType(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.officeTypeId, self.name))

class OfficeBranch(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.officeBranchId, self.name))

class OfficeLevel(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.officeLevelId, self.name))


class Office(APIMethodBase):

    def getTypes(self):
        result = self.api.api_call('Office.getTypes', {})
        return self.result_to_obj(OfficeType, result['officeTypes']['type'])

    def getBranches(self):
        result = self.api.api_call('Office.getBranches', {})
        return self.result_to_obj(OfficeBranch, result['branches']['branch'])

    def getLevels(self):
        result = self.api.api_call('Office.getLevels', {})
        return self.result_to_obj(OfficeLevel, result['levels']['level'])

    def getOfficesByType(self, typeId):
        params = {'officeTypeId':typeId}
        result = self.api.api_call('Office.getOfficesByType', params)
        return self.result_to_obj(OfficeData, result['offices']['office'])

    def getOfficesByLevel(self, levelId):
        params = {'levelId':levelId}
        result = self.api.api_call('Office.getOfficesByLevel', params)
        return self.result_to_obj(OfficeData, result['offices']['office'])

    def getOfficesByTypeLevel(self, officeTypeId, levelId):
        params = {'officeTypeId':officeTypeId, 'officeLevelId':levelId}
        result = self.api.api_call('Office.getOfficesByTypeLevel', params)
        return self.result_to_obj(OfficeData, result['offices']['office'])

    def getOfficesByBranchLevel(self, branchId, levelId):
        params = {'branchId':branchId, 'levelId':levelId}
        result = self.api.api_call('Office.getOfficesByBranchLevel', params)
        return self.result_to_obj(OfficeData, result['offices']['office'])
