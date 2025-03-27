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
    
    #Вычисление значения дроби с округлением
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

print("Задание №2")
from fractions import Fraction

class FractionMatrix:
    def __new__(cls, matrix):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Матрица должна быть списком списков.")
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise ValueError("Все строки матрицы должны иметь одинаковую длину.")
        if any(not all(isinstance(elem, (int, Fraction)) for elem in row) for row in matrix):
            raise ValueError("Элементы матрицы должны быть целыми числами или дробями.")
        return super().__new__(cls)

    def __init__(self, matrix):
        self.matrix = [[Fraction(elem) for elem in row] for row in matrix]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    @staticmethod
    def check_dimensions(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Размеры матриц не совпадают.")

    @classmethod
    def identity_matrix(cls, n):
        identity = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
        return cls(identity)

    def __add__(self, other):
        if not isinstance(other, FractionMatrix):
            raise TypeError("Операция возможна только между объектами FractionMatrix.")
        self.check_dimensions(self, other)
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __sub__(self, other):
        if not isinstance(other, FractionMatrix):
            raise TypeError("Операция возможна только между объектами FractionMatrix.")
        self.check_dimensions(self, other)
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __mul__(self, other):
        if isinstance(other, FractionMatrix):
            if self.cols != other.rows:
                raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй.")
            result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) 
                       for j in range(other.cols)] for i in range(self.rows)]
            return FractionMatrix(result)
        elif isinstance(other, (int, Fraction)):
            result = [[elem * other for elem in row] for row in self.matrix]
            return FractionMatrix(result)
        else:
            raise TypeError("Неверный тип аргумента.")

    def transpose(self):
        transposed = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return FractionMatrix(transposed)

    @property
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратной матрицы.")
        if self.rows == 1:
            return self.matrix[0][0]
        if self.rows == 2:
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        det = Fraction(0)
        for col in range(self.cols):
            minor = FractionMatrix([row[:col] + row[col+1:] for row in self.matrix[1:]])
            sign = (-1)**(col % 2)
            det += sign * self.matrix[0][col] * minor.determinant
        return det

    def __repr__(self):
        rows = ["[" + ", ".join(str(Fraction(elem).limit_denominator()) for elem in row) + "]" for row in self.matrix]
        return "\n".join(rows)

# Пример использования
if __name__ == "__main__":
    m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
    m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
    print(m1 + m2)  # Сложение матриц
    print(m1 * m2)  # Умножение матриц
    print(m1.transpose())  # Транспонирование матрицы
    print(m1.determinant)  # Определитель матрицы