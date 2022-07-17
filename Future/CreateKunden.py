import random

class Kunde:
    def __init__(self, name, id, old):
        self.name = name
        self.id = id
        self.old = old

if __name__ == '__main__':
    import pickle

    names = ['Gustav', 'Lucas', 'Simon', 'Paul', 'Tim']

    for i in range(24):
        kunde = Kunde(random.choice(names), i, random.randint(1, 70))
        file = open(f'./kundenj/{i}kunde.kunde', 'wb')
        pickle.dump(kunde, file, pickle.HIGHEST_PROTOCOL)