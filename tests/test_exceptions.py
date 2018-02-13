import pytest
from votesmart.exceptions import VotesmartApiError

def test_sanity():
    assert 1 + 1 == 2

def test_VotesmartApiError():
    with pytest.raises(VotesmartApiError):
        raise VotesmartApiError()
