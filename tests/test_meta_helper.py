import six
from votesmart.meta_helper import OuterMeta

@six.add_metaclass(OuterMeta)
class Outer:
    def foo(self):
        return "I'm outer class!"

    class Inner(object):
        outer = None  # <-- by default it's None

        def bar(self):
            return "I'm inner class"


def test_instance():
    assert isinstance(Outer.Inner.outer(), Outer)

    assert Outer().foo() == "I'm outer class!"
    assert Outer.Inner.outer().foo() == "I'm outer class!"
    assert Outer.Inner().bar() == "I'm inner class"
