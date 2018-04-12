"""
Candidates methods that correspond to this API documentation page

http://api.votesmart.org/docs/Candidates.html
"""


from .base import APIMethodBase
from .containers import Candidate


class Candidates(APIMethodBase):

    def getByOfficeState(self, officeId, stateId=None, electionYear=None, stageId=None):
        params = {'officeId': officeId, 'stateId':stateId, 'electionYear': electionYear, "stageId": stageId}
        result = self.api.api_call('Candidates.getByOfficeState', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByOfficeTypeState(self, officeTypeId, stateId=None, electionYear=None):
        params = {'officeTypeId': officeTypeId, 'stateId':stateId, 'electionYear': electionYear}
        result = self.api.api_call('Candidates.getByOfficeTypeState', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByLastname(self, lastName, electionYear=None):
        params = {'lastName': lastName, 'electionYear':electionYear}
        result = self.api.api_call('Candidates.getByLastname', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByLevenstein(self, lastName, electionYear=None):
        params = {'lastName': lastName, 'electionYear':electionYear}
        result = self.api.api_call('Candidates.getByLevenstein', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByElection(self, electionId, stageId=None):
        params = {'electionId': electionId, 'stageId': stageId}
        result = self.api.api_call('Candidates.getByElection', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByDistrict(self, districtId, electionYear=None):
        params = {'districtId': districtId, 'electionYear':electionYear}
        result = self.api.api_call('Candidates.getByDistrict', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByZip(self, zip5, electionYear=None, zip4=None):
        # errors on zip 20001
        params = {'zip4': zip4, 'zip5': zip5, 'electionYear':electionYear}
        result = self.api.api_call('Candidates.getByZip', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])
