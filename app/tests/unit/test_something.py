from . import TextMixin

class Something(TextMixin):

    def test_something(self):
        assert False

    def test_something2(self):
        assert True