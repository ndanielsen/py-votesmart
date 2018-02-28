from __future__ import print_function
from votesmart import utils as uts
from votesmart.containers import *


def test_sanity():
    assert 1 + 1 == 2

def test_VotesmartApiObject():
    data = {"hello": "friend"}
    result = VotesmartApiObject(data)
    assert result.hello == "friend"
