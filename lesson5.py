import math
print("Задание №1")
class Fraction:
    def __init__(self, numerator:int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Числитель и знаменатель дорлжны быть целыми!")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю!")
        self._numerator = numerator
        self._denominator = denominator
    
    def reduce(self):
      gcd = math.gcd(self.numerator, self.denominator)
      self.numerator //= gcd
      self.denominator //= gcd
      if self.denominator < 0:
          self.numerator *= -1
          self.denominator *= -1
      return Fraction(self.numerator, self.denominator)
    
    #Вычисление точного значения дроби с округлением до 3-го знака.
    @property 
    def value(self):
        return round(self._numerator / self._denominator, 3)
    
    #Красивый вывод дроби (a/b).
    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
    
    #Сложение
    def __add__(self, other):
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)
    #Вычитание
    def __sub__(self, other):
        new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)
    #Умножение
    def __mul__(self, other):
        new_numerator = self._numerator *  other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)
    #Деление
    def __truediv__(self, other):
        new_numerator = self._numerator *  other._denominator
        new_denominator = self._denominator * other._numerator
        return Fraction(new_numerator, new_denominator)



f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  # 5/4
print(f1 - f2)  # -1/4
print(f1 * f2)  # 3/8
print(f1 / f2)  # 2/3
print(f1.value) # 0.5







#Красивый вывод дроби (a/b).
#Все возможные проверки (целые числа в числителе и знаменателе, отрицательные значения и т. д.).
#Использование staticmethod, classmethod, __new__, property.