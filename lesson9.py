#Задание №1
import math
class Shape:
    def area(self): #Площадь
        raise NotImplementedError("Метод area() должен быть определен")
    
    def perimeter(self): #Периметр
        raise NotImplementedError("Метод perimeter() должен быть определен")
#Круг
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
#Прямоугольник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
# Пример использования
circle = Circle(5)
print("Circle area:", round(circle.area(),3))
print("Circle perimeter:", round(circle.perimeter(),3))

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

#Задание №2
class Animal:
    def sound(self):
        return "Звуки животного"
#Dog
class Dog(Animal):
    def sound(self):
        return "Гав-гав"
#Cat
class Cat(Animal):
    def sound(self):
        return "Мяу"
#Cow
class Cow(Animal):
    def sound(self):
        return "Муу"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())