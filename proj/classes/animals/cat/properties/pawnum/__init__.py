from functools import cached_property


@cached_property
def pawnum(self):
    return self.number_of_front_legs + self.number_of_hind_legs
