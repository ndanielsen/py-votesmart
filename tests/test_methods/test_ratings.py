import pytest
from votesmart.methods.ratings import *

def test_Rating():
    with pytest.raises(NotImplementedError):
        method = Rating(api_instance='test')
