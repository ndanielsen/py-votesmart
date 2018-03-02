import pytest
from votesmart.methods.address import *

def test_Address():
    with pytest.raises(NotImplementedError):

        method = Address(api_instance='test')
