"""Command functions instances for API Calls
"""


class APIMethodBase:
    def __init__(self, api_instance):
        self.api = api_instance

    def result_to_obj(self, cls, result):
        "Convert a dict / list response into a list of parsed elements"
        if isinstance(result, dict):
            return [cls(result)]
        else:
            # the if o predicate is important, sometimes they return empty strings
            return [cls(o) for o in result if o]
