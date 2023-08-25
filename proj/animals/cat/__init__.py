from proj.animals.cat.properties import CatProperties


class Cat(CatProperties):

    def __init__(self, number_of_front_legs=2, number_of_hind_legs=2):
        self.number_of_front_legs = number_of_front_legs
        self.number_of_hind_legs = number_of_hind_legs
