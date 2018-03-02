import pytest
from votesmart.methods.district import *

def test_District():
    with pytest.raises(NotImplementedError):

        method = District(api_instance='test')
