import pytest
from votesmart.methods.votes import *

def test_Votes():
    with pytest.raises(NotImplementedError):
        method = Votes(api_instance='test')
