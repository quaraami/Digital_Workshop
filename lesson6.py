import math
import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    """Дескриптор для вычисления производной функции"""
    
    def __init__(self, func):
        """ Инициализация дескриптора :param func:param функция, для которой будет вычисляться производная """
        self.func = func

    def __get__(self, instance, owner):
        """ Возвращаем либо сам дескриптор, либо функцию для вычисления производной, в зависимости от контекста вызова :param instance: экземпляр класса, владеющего данным дескриптором :param owner: класс, владеющий данным дескриптором :return: дескриптор или функцию для вычисления производной """
        if instance is None:
            return self
        return lambda x: self.__call__(instance, x)

    def __call__(self, instance, x):
        """ Вычисление производной функции в точке x численным методом :param instance: экземпляр класса, владеющего данным дескриптором :param x: точка, в которой нужно вычислить производную :return: приближенное значение производной """
        h = 1e-5  # малое смещение для численной аппроксимации
        return (instance(x + h) - instance(x - h)) / (2 * h)


class ExponentialFunction:
    """Класс для представления функции вида f(x) = a * e^x"""
    
    def __init__(self, a):
        """ Инициализация объекта функции :param a: коэффициент перед экспонентой """
        self.a = a
        self.derivative = Derivative(self)

    def __call__(self, x):
        """ Вызов объекта функции как обычной функции :param x: аргумент функции :return: значение функции в точке x """
        return self.a * math.exp(x)

    def plot(self, start=-2, end=2, num_points=200):
        """ Построение графиков функции и её производной :param start: начальная точка интервала :param end: конечная точка интервала :param num_points: количество точек для графика """
        x_values = np.linspace(start, end, num_points)
        y_values = [self(x) for x in x_values]
        dy_values = [self.derivative(x) for x in x_values]

        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=r'$f(x)$', color='blue')
        plt.plot(x_values, dy_values, label=r"$f'(x)$", linestyle='--', color='red')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$')
        plt.title(f'График функции $f(x)={self.a}e^{{{x}}}$ и её производной')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()


# Пример использования
if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)
    print("Значение функции в точке x=0:", exp_func(0))       # Должно вывести 2.0
    print("Производная функции в точке x=0:", exp_func.derivative(0))  # Должно вывести 2.0

    # Построение графиков
    exp_func.plot()