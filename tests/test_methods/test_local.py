import pytest
from votesmart.methods.local import *

def test_Local():
    with pytest.raises(NotImplementedError):
        method = Local(api_instance='test')
