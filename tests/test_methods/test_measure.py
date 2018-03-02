import pytest
from votesmart.methods.measure import *

def test_Measure():
    with pytest.raises(NotImplementedError):
        method = Measure(api_instance='test')
