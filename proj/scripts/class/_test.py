from functions import class_fun, attr_fun


def test_class():

    try:
        class_fun('create')

        from proj.classes.animals.dog import Dog
        dog = Dog()
        assert dog.sound == 'whoof'
    finally:
        class_fun('delete')


def test_attr():

    try:
        class_fun('create')
        attr_fun()

        from proj.classes.animals.dog import Dog
        dog = Dog()
        assert dog.ability == 'fetch stick'
    finally:
        class_fun('delete')
