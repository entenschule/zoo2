from functools import cached_property


@cached_property
def clawnum(self):
    return self.number_of_legs * 5
