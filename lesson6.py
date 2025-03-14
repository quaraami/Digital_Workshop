import matplotlib.pyplot as plt
import numpy as np
class Derivate:
    def __init__(self, func, h=1e-5):
        self.func = func
        self.h = h
        self.instance = None

    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

class ExponentialFunction:
    def __init__(self, a):
        self.a = a

    def __call__(self, x):
        return self.a * (np.exp ** x)


exp_func = ExponentialFunction(a=1)

x_values = np.linspace(-2, 2, 1000)

y_values = exp_func(x_values)
dy_values = exp_func.instance(x_values)

# Строим графики
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x)')
plt.plot(x_values, dy_values, label="f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции и её производной')
plt.legend()
plt.grid(True)
plt.show()