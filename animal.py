class Animal:
    def __init__(self):
        self.legs=4
        self.domastic=True
        self.tail=True
        self.mammal=True

    def isMammal(self):
        if self.mammal:
            print('It is a mammal')

    def isDomastic(self):
        if self.domastic:
            print('It is a domastic animal')
class Dogs(Animal) :
    def __init__(self):
        super().isMammal()


class Horses(Animal):
    def __init__(self):
        pass