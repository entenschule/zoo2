from proj.classes.animals.cat import Cat


def test():
    standard_cat = Cat()
    assert standard_cat.clawnum == 18

    limping_cat = Cat(number_of_hind_legs=1)
    assert limping_cat.clawnum == 14

    stationary_cat = Cat(number_of_front_legs=0, number_of_hind_legs=0)
    assert stationary_cat.clawnum == 0
