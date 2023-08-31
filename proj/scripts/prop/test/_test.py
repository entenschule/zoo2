import os
import pytest

from proj.scripts.prop.function import prop_fun


this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(os.path.dirname(this_folder)))
properties_folder = os.path.join(proj_folder, 'classes', 'animals', 'cat', 'properties')


def test_created_prop():
    try:
        prop_fun('create', 'animals.cat', 'foo')

        from proj.classes.animals.cat.properties.names import names
        assert 'foo' in names  # this works

        property_folder_names = [f.name for f in os.scandir(properties_folder) if f.is_dir()]
        assert 'foo' in property_folder_names  # this works

        from proj.classes.animals.cat import Cat
        cat = Cat()
        assert hasattr(cat, 'foo')
        assert cat.foo == 'dummy result of property foo'
    finally:
        prop_fun('delete', 'animals.cat', 'foo')


def test_deleted_prop():
    try:
        prop_fun('delete', 'animals.cat', 'whiskers')

        from proj.classes.animals.cat.properties.names import names
        assert 'whiskers' not in names  # this works

        property_folder_names = [f.name for f in os.scandir(properties_folder) if f.is_dir()]
        assert 'whiskers' not in property_folder_names  # this works

        from proj.classes.animals.cat import Cat
        cat = Cat()
        assert not hasattr(cat, 'whiskers')
        with pytest.raises(AttributeError, match="'Cat' object has no attribute 'whiskers'"):
            cat.whiskers
    finally:
        prop_fun('create', 'animals.cat', 'whiskers')
