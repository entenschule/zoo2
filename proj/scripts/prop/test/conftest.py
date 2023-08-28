import pytest

from proj.scripts.prop.function import prop_fun


@pytest.fixture(scope='session')
def prop_foo():
    prop_fun('create', 'animals.cat', 'foo')
