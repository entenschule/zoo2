import os
import pytest

from proj.scripts.prop.function import create_or_delete_property


this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(os.path.dirname(this_folder)))
properties_folder = os.path.join(proj_folder, 'classes', 'animals', 'cat', 'properties')
properties_file = os.path.join(proj_folder, 'classes', 'animals', 'cat', 'properties', '__init__.py')


def test_created_prop_extensive():
    try:
        create_or_delete_property('create', 'animals.cat', 'foo')

        from proj.classes.animals.cat.properties.names import names
        assert 'foo' in names  # works

        property_folder_names = [f.name for f in os.scandir(properties_folder) if f.is_dir()]
        assert 'foo' in property_folder_names  # works

        with open(properties_file) as f:
            assert "from .foo import foo" in f.read()  # works

        from proj.classes.animals.cat.properties import CatProperties
        assert hasattr(CatProperties, 'foo')  # FAILS

        from proj.classes.animals.cat import Cat
        assert hasattr(Cat, 'foo')  # FAILS
        cat = Cat()
        assert cat.foo == 'dummy result of property foo'  # FAILS
    finally:
        create_or_delete_property('delete', 'animals.cat', 'foo')


def test_deleted_prop_extensive():
    try:
        create_or_delete_property('delete', 'animals.cat', 'whiskers')

        from proj.classes.animals.cat.properties.names import names
        assert 'whiskers' not in names  # works

        property_folder_names = [f.name for f in os.scandir(properties_folder) if f.is_dir()]
        assert 'whiskers' not in property_folder_names  # works

        with open(properties_file) as f:
            assert "from .whiskers import whiskers" not in f.read()  # works

        from proj.classes.animals.cat.properties import CatProperties
        assert not hasattr(CatProperties, 'whiskers')  # FAILS

        from proj.classes.animals.cat import Cat
        assert not hasattr(Cat, 'whiskers')  # FAILS
        cat = Cat()
        with pytest.raises(AttributeError, match="'Cat' object has no attribute 'whiskers'"):
            cat.whiskers  # FAILS
    finally:
        create_or_delete_property('create', 'animals.cat', 'whiskers')
