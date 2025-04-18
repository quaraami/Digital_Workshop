print("Задание №1")
class Animal:
    def speak(self):
        return 'Издает звук'
    
class MixinSwim:
    def swim(self):
        return 'Плавает'

class MixinFly:
    def fly(self):
        return 'Летает'

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return 'Кря-кря'

class Penguin(Animal, MixinSwim):
    def speak(self):
        return 'Буль-буль'

animals = [Duck(), Penguin()]

for animal in animals:
    print(f'Животное говорит: {animal.speak()}')
    print(f'{type(animal).__name__}: {animal.swim()}')
    if isinstance(animal, MixinFly):
        print(f'{type(animal).__name__}: {animal.fly()}')

print("Задание №2")
class Writer:
    def write(self):
        return 'пишет текст'

class Painter:
    def draw(self):
        return 'рисует картину'

class CreativePerson(Writer, Painter):
    def write(self):
        return 'творчески пишет стихотворение'
    
    def draw(self):
        return 'выразительно рисует пейзаж'

creatives = [Writer(),Painter(),CreativePerson()]

for person in creatives:
    if hasattr(person, 'write'):
        print(f'{type(person).__name__}: {person.write()}')
    if hasattr(person, 'draw'):
        print(f'{type(person).__name__}: {person.draw()}')
