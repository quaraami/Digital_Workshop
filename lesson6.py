import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, h=10**(-5)):
        self.func=None
        self.h = h
    def __get__(self, func, owner):
        self.func = func
        return self
    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

class ExponentialFunction:
    derivative = Derivative(10**(-5))
    def __init__(self, a):
        self.a = a
    def __call__(self, x):
        return self.a * np.exp(x)
    def plot(self):
        x = np.linspace(-2, 2, 500)
        y = self(x)
        dy = self.derivative(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='f(x) = a * e^x', color='red')
        plt.plot(x, dy, label="f'(x)", linestyle='dashed', color='blue')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel("f(x) и f'(x)")
        plt.title('Графики функции и её производной')
        plt.grid()
        plt.show()

exp_func = ExponentialFunction(a=2)
print(exp_func(0))         
print(exp_func.derivative(0))
exp_func.plot()