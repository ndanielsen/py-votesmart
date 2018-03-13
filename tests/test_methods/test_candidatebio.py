import pytest
from votesmart.methods.candidatebio import *

def test_CandidateBio():
    method = CandidateBio(api_instance='test')


def test_Bio():
    d = {"candidate": {"items": 'ok', "something": 'value'}, 'story': "blah"}
    obj = Bio(d)


def test_AddlBio():
    AddlBio({"candidate": 'hello'})
