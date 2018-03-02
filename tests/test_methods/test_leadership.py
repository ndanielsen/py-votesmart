import pytest
from votesmart.methods.leadership import *

def test_Leadership():
    with pytest.raises(NotImplementedError):
        method = Leadership(api_instance='test')
