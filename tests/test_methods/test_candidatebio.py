import pytest
from votesmart.methods.candidatebio import *

def test_CandidateBio():
    with pytest.raises(NotImplementedError):
        method = CandidateBio(api_instance='test')
