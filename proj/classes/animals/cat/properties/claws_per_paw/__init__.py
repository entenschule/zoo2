from functools import cached_property


@cached_property
def claws_per_paw(self):

    if self.pawnum == 0:
        return

    return self.clawnum / self.pawnum
