"""Containers to hold individual data items in a response
"""

class VotesmartApiObject(object):
    def __init__(self, d):
        self.__dict__ = d

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)
