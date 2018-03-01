from .base import APIMethodBase
from .containers import VotesmartApiObject

class Candidate(VotesmartApiObject):
    def __str__(self):
        return ' '.join((self.firstName, self.lastName))

class Candidates(APIMethodBase):

    def getByOfficeState(self, officeId, stateId=None, electionYear=None):
        params = {'officeId': officeId, 'stateId':stateId, 'electionYear': electionYear}
        result = self.api.api_call('Candidates.getByOfficeState', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByOfficeState(self, officeId, stateId=None, electionYear=None):
        params = {'officeId': officeId, 'stateId':stateId, 'electionYear': electionYear}
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

    def getByElection(self, electionId):
        params = {'electionId': electionId}
        result = self.api.api_call('Candidates.getByElection', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByDistrict(self, districtId, electionYear=None):
        params = {'districtId': districtId, 'electionYear':electionYear}
        result = self.api.api_call('Candidates.getByDistrict', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])

    def getByZip(self, zip5, zip4=None):
        params = {'zip4': zip4, 'zip5': zip5}
        result = self.api.api_call('Candidates.getByZip', params)
        return self.result_to_obj(Candidate, result['candidateList']['candidate'])