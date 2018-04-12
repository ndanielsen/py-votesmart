"""
Rating methods that correspond to this API documentation page

http://api.votesmart.org/docs/Rating.html
"""

from .base import APIMethodBase
from .containers import VotesmartApiObject

class Category(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.categoryId, self.name))

class Sig(VotesmartApiObject):
    def __str__(self):
        return ': '.join((self.sigId, self.name))

class SigDetail(VotesmartApiObject):
    def __str__(self):
        return self.name

class RatingObject(VotesmartApiObject):
    def __str__(self):
        return self.ratingText

class Rating(APIMethodBase):

    def getCategories(self, stateId=None):
        params = {'stateId':stateId}
        result = self.api.api_call('Rating.getCategories', params)
        return self.result_to_obj(Category, result['categories']['category'])

    def getSigList(self, categoryId, stateId=None):
        params = {'categoryId':categoryId, 'stateId':stateId}
        result = self.api.api_call('Rating.getSigList', params)
        return self.result_to_obj(Sig, result['sigs']['sig'])

    def getSig(self, sigId):
        params = {'sigId':sigId}
        result = self.api.api_call('Rating.getSig', params)
        return SigDetail(result['sig'])

    def getSigRatings(self, sigId):
        params = {'sigId':sigId}
        result = self.api.api_call('Rating.getSigRatings', params)
        #TODO Fix this
        return VotesmartApiObject(result['sigRatings'])

    def getCandidateRating(self, candidateId, sigId=None):
        params = {'candidateId':candidateId, 'sigId':sigId}
        result = self.api.api_call('Rating.getCandidateRating', params)
        return self.result_to_obj(RatingObject, result['candidateRating']['rating'])

    def getRating(self, ratingId):
        params = {'ratingId':ratingId}
        result = self.api.api_call('Rating.getRating', params)
        return self.result_to_obj(VotesmartApiObject, result['rating']['candidateRating'])
