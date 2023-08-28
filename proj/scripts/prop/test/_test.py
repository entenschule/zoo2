from proj.classes.animals.cat import Cat


def test(prop_foo):
    cat = Cat()
    assert cat.foo == 'dummy result of property foo'
