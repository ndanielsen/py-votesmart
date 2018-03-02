from votesmart.methods.containers import VotesmartApiObject
from votesmart.methods.base import *

def test_result_to_obj():
    data = {}
    data['address'] = '123 address'
    data['phone'] = ['623-232-2321']
    data['notes'] = [" a note"]

    obj = APIMethodBase(api_instance="fake instance")

    result = obj.result_to_obj(VotesmartApiObject, data)
    assert 1 == len(result)
    assert result[0].address == '123 address'
