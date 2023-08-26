from proj.classes.animals.cat import Cat


def test():
    standard_cat = Cat()
    assert standard_cat.pawnum == 4

    limping_cat = Cat(number_of_hind_legs=1)
    assert limping_cat.pawnum == 3

    stationary_cat = Cat(number_of_front_legs=0, number_of_hind_legs=0)
    assert stationary_cat.pawnum == 0
