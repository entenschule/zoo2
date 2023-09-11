from functions import create_class, delete_class, add_attribute
from proj.scripts.prop.function import create_or_delete_property


def test_class():

    try:
        create_class()

        from proj.classes.animals.dog import Dog
        dog = Dog()
        assert dog.sound == 'whoof'
        assert dog.clawnum == 20
    finally:
        delete_class()


def test_attr():

    try:
        create_class()
        add_attribute()

        from proj.classes.animals.dog import Dog
        dog = Dog()
        assert dog.ability == 'fetch stick'
    finally:
        delete_class()


def test_new_prop():
    try:
        create_class()
        create_or_delete_property('create', 'animals.dog', 'foo')

        from proj.classes.animals.dog import Dog
        dog = Dog()
        assert dog.foo == 'dummy result of property foo'
    finally:
        delete_class()
