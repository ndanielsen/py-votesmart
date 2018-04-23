"""
Measure methods that correspond to this API documentation page

http://api.votesmart.org/docs/Measure.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class MeasureList(VotesmartApiObject):
    def __str__(self):
        return self.title

class MeasureDetail(VotesmartApiObject):
    def __str__(self):
        return self.title


class Measure(APIMethodBase):

    def getMeasuresByYearState(self, year, stateId):
        params = {'year':year, 'stateId':stateId}
        result = self.api.api_call('Measure.getMeasuresByYearState', params)
        return self.result_to_obj(MeasureList, result['measures']['measure'])

    def getMeasure(self, measureId):
        params = {'measureId':measureId}
        result = self.api.api_call('Measure.getMeasure', params)
        return MeasureDetail(result['measure'])
