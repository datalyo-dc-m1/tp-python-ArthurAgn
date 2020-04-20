class Monkey:
    def __init__(self, name):
        self.name = name
    def eat(self,banane):
        print(self.name, 'mange une banane', banane.color)

class Banane:
    def __init__(self,color):
        self.color = color

banane_verte = Banane('verte')
banane_jaune = Banane('jaune')
pierre = Monkey('Pierre')
marie = Monkey('Marie')

pierre.eat(banane_jaune)
marie.eat(banane_verte)