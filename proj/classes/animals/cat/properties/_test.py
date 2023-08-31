import pytest

from proj.classes.animals.cat import Cat


def test_known_prop():
    cat = Cat()
    assert hasattr(cat, 'whiskers')
    assert cat.whiskers == 'dummy result of property whiskers'


def test_unknown_prop():
    cat = Cat()
    assert not hasattr(cat, 'foo')
    with pytest.raises(AttributeError, match="'Cat' object has no attribute 'foo'"):
        cat.foo
