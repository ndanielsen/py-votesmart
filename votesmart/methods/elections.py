"""
Election methods that correspond to this API documentation page

http://api.votesmart.org/docs/Election.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject, Candidate
from .utils import result_to_obj

class ElectionData(VotesmartApiObject):
    def __init__(self, d):
        stages = d.pop('stage', None)
        self.__dict__ = d
        if stages:
            self.stages = result_to_obj(ElectionStage, stages)

    def __str__(self):
        return self.name

class ElectionStage(VotesmartApiObject):
    def __str__(self):
        return '%s (%s)' % (self.name, self.electionDate)


class Election(APIMethodBase):

    def getElection(self, electionId):
        params = {'electionId':electionId}
        result = self.api.api_call('Election.getElection', params)
        return ElectionData(result['elections']['election'])

    def getElectionByYearState(self, year, stateId=None):
        params = {'year':year, 'stateId':stateId}
        result = self.api.api_call('Election.getElectionByYearState', params)
        return self.result_to_obj(ElectionData, result['elections']['election'])

    def getElectionByZip(self, zip5, zip4=None, year=None):

        params = {'zip5': zip5, 'zip4': zip4, 'year': year}
        result = self.api.api_call('Election.getElectionByZip', params)
        return self.result_to_obj(ElectionData, result['elections']['election'])

    def getStageCandidates(self, electionId, stageId, party=None,
                           districtId=None, stateId=None):

        params = {'electionId':electionId, 'stageId':stageId,
                  'party':party, 'districtId':districtId, 'stateId':stateId}
        result = self.api.api_call('Election.getStageCandidates', params)
        return self.result_to_obj(Candidate, result['stageCandidates']['candidate'])
