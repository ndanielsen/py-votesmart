"""
Npat methods that correspond to this API documentation page

Political Courage Test

Returns a candidates most recently filled out Political Courage Test.

http://api.votesmart.org/docs/Npat.html
"""

from .base import APIMethodBase

class Npat(APIMethodBase):

    def getNpat(self, candidateId):
        params = {'candidateId':candidateId}
        result = self.api.api_call('Npat.getNpat', params)
        return result['npat']
