from proj.classes.animals.cat import Cat

from pytest import approx


def test():

    cat_2_2 = Cat()
    cat_1_1 = Cat(number_of_front_legs=1, number_of_hind_legs=1)
    assert cat_2_2.claws_per_paw == cat_1_1.claws_per_paw == 4.5

    cat_2_1 = Cat(number_of_hind_legs=1)
    assert cat_2_1.claws_per_paw == approx(4.666666)  # 14 /3

    cat_1_2 = Cat(number_of_front_legs=1)
    assert cat_1_2.claws_per_paw == approx(4.333333)  # 13 / 3

    cat_2_0 = Cat(number_of_hind_legs=0)
    cat_1_0 = Cat(number_of_front_legs=1, number_of_hind_legs=0)
    assert cat_2_0.claws_per_paw == cat_1_0.claws_per_paw == 5

    cat_0_2 = Cat(number_of_front_legs=0)
    cat_0_1 = Cat(number_of_front_legs=0, number_of_hind_legs=1)
    assert cat_0_2.claws_per_paw == cat_0_1.claws_per_paw == 4

    cat_0_0 = Cat(number_of_front_legs=0, number_of_hind_legs=0)
    assert cat_0_0.claws_per_paw is None
