import pytest
from votesmart.methods.npat import *

def test_Npat():
    with pytest.raises(NotImplementedError):
        method = Npat(api_instance='test')
