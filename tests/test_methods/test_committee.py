import pytest
from votesmart.methods.committee import *

def test_Committee():
    with pytest.raises(NotImplementedError):
        method = Committee(api_instance='test')
