from proj.classes.animals.dog.properties import DogProperties


class Dog(DogProperties):

    def __init__(self, number_of_legs=4):
        self.number_of_legs = number_of_legs

    sound = 'whoof'
