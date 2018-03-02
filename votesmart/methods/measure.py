"""
Measure methods that correspond to this API documentation page

http://api.votesmart.org/docs/Measure.html
"""

from .base import APIMethodBase

class Measure(APIMethodBase):
    def __init__(self, api_instance):
        raise NotImplementedError()
#     class Measure(object):
#         @staticmethod
#         def getMeasuresByYearState(year, stateId):
#             params = {'year':year, 'stateId':stateId}
#             result = votesmart._apicall('Measure.getMeasuresByYearState', params)
#             return _result_to_obj(Measure, result['measures']['measure'])
#
#         @staticmethod
#         def getMeasure(measureId):
#             params = {'measureId':measureId}
#             result = votesmart._apicall('Measure.getMeasure', params)
#             return MeasureDetail(result['measure'])
#
