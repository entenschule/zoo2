import os
import pytest

from proj.scripts.prop.function import create_or_delete_property


this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(os.path.dirname(this_folder)))
properties_folder = os.path.join(proj_folder, 'classes', 'animals', 'cat', 'properties')
properties_file = os.path.join(proj_folder, 'classes', 'animals', 'cat', 'properties', '__init__.py')


def test_created_prop():
    try:
        create_or_delete_property('create', 'animals.cat', 'foo')

        from proj.classes.animals.cat import Cat
        cat = Cat()
        assert cat.foo == 'dummy result of property foo'

    finally:
        create_or_delete_property('delete', 'animals.cat', 'foo')


def test_deleted_prop():
    try:
        create_or_delete_property('delete', 'animals.cat', 'whiskers')

        from proj.classes.animals.cat import Cat
        cat = Cat()
        with pytest.raises(AttributeError, match="'Cat' object has no attribute 'whiskers'"):
            cat.whiskers

    finally:
        create_or_delete_property('create', 'animals.cat', 'whiskers')
