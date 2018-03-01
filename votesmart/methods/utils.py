from ..exceptions import VotesmartApiError

def parse_api_response(response):
    if response.get('error'):
        raise VotesmartApiError(response['error']['errorMessage'])
    else:
        return response

def result_to_obj(cls, result):
    "Convert a dict / list response into a list of parsed elements"
    if isinstance(result, dict):
        return [cls(result)]
    else:
        # the if o predicate is important, sometimes they return empty strings
        return [cls(o) for o in result if o]
