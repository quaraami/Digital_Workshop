#Задание №4
import math
class Vector:
    def __init__(self, *args):
        for coord in args:
            if not isinstance(coord, (int, float)):
                raise TypeError("Все координаты вектора должны быть числами.")
        self.coords = list(args)

    def __len__(self): #кол-во координат
        return len(self.coords)

    def __abs__(self): #евклидова норма
        sum_of_squares = sum(coord ** 2 for coord in self.coords)
        return math.sqrt(sum_of_squares)
    

v = Vector(1, 2, 3)
print(len(v))      #3
print(abs(v))      #3.7416573867739413

v = Vector(0, -5)
print(len(v))      # 2
print(abs(v))      # 5.0

try:
    v = Vector("a", 2)
except TypeError as e:
    print(e)       # TypeError

#Задание №3
class CacheCalculator:
    def __init__(self):
        self._cache = {}
    
    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError(f"Аргумент должен быть int, а не {type(x).__name__}")
        
        if x in self._cache:
            return self._cache[x]
        
        result = x ** 2
        self._cache[x] = result
        return result

    @property
    def cache(self):
        return self._cache
calc = CacheCalculator()
result_1 = calc(2)
print(result_1)      # Выводит: 4
print(calc.cache)    # Выводит: {2: 4}
result_2 = calc(2.5)
print(result_2)      # Выводит: 6.25
print(calc.cache)    # Выводит: {2: 4, 2.5: 6.25}

try:
    calc("text")
except TypeError as error:
    print(error)         # Выводит: TypeError