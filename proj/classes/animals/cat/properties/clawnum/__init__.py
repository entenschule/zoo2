from functools import cached_property


@cached_property
def clawnum(self):
    return self.number_of_front_legs * 5 + self.number_of_hind_legs * 4
