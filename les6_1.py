import random
# class SomeClass:
#     name = 'somename'

class Car:
    population = []

    def __init__(self, color, year, brand, model):
        self.color = color
        self.year = year
        self. brand = brand
        self.model = model
        self.population.append(self)

    def run(self):
        print('DRDRDR')

ford_t = Car('Black', '1920', 'Ford', 'Model T')
tesla_s = Car('Red', '2009', 'Tesla', 'Model S')

print(Car.population[0].model)
print(tesla_s.population)

tesla_s.new_attr = 'NEW'

class Wolf:
    _some_protected = 'Protected'
    __some_private = 'PRIVATE'

    def __init__(self, color, height, sex):
        self.color = color
        self.height = height
        self.sex = sex

    def say(self):
        print('RRRRRRRAAAAYYYYYYYYY')

class Dog(Wolf):

    def __init__(self, name, color, height):
        super().__init__(color, height, random.choice('f', 'm'))
        self.name = name

    def say(self):
        print('WOFFFF')


