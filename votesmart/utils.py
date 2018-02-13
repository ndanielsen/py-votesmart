from .exceptions import VotesmartApiError

def _parse_api_response(response):
    if response.get('error'):
        raise VotesmartApiError(response['error']['errorMessage'])
    else:
        return response
