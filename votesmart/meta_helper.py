"""Adding in meta class support to allow the api data call methods to access
the parent class

Code found here:
https://stackoverflow.com/questions/2024566/access-outer-class-from-inner-class-in-python
"""

import inspect

# helper method to add metaclass
_METACLASS_ = '_metaclass_helper_'
def with_metaclass(meta, base=object):
    return meta(_METACLASS_, (base,), {})

class OuterMeta(type):
    def __new__(mcs, name, parents, dct):
        cls = super(OuterMeta, mcs).__new__(mcs, name, parents, dct)
        for klass in dct.values():
            if inspect.isclass(klass):
                klass.outer = cls

        return cls
