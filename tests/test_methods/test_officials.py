import pytest
from votesmart.methods.officials import *

def test_Officials():
    with pytest.raises(NotImplementedError):
        method = Officials(api_instance='test')
