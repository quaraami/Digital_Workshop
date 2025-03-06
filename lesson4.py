print("Задание №1")
class Person:
    def __init__(self, name, surname, age):
            self.name = name  
            self.age = age
            self.surname = surname
    def __setattr__(self, key, value):
        if key == 'name':
            if not isinstance(value, str) or len(value) == 0:
                raise ValueError("Name must consist of letters and cannot be empty!")
        elif key == 'surname':
             if not isinstance(value, str) or len(value) == 0:
                raise ValueError("Surname must consist of letters and cannot be empty!")
        elif key == 'age':
            if not isinstance(value, (int)) or value <= 0:
                raise ValueError("Age must be a whole, positive number!")
        super().__setattr__(key, value)
person = Person("John", "Watson", 25)
print(f"Имя: {person.name}, Фамилия: {person.surname}, Возраст: {person.age}")

p = Person("Alice", "Parker", 30)  
print(p.name, p.surname, p.age)

p2 = Person("Тимофей", "Шумилов", 18)  
p2.name = ""
p2.surname = 1324             
p2.age = -5

print("Задание №3")
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, attr_name):
        if attr_name in ["make", "model"]:
            raise AttributeError(f"'Car' object has no attribute '{attr_name}'")
        return "This attribute is not available"

c = Car("Toyota", "Corolla")
print(c.make)     
print(c.color) 

print("Задание №4")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'width' or name == 'height':
            super().__setattr__(name, value)
        elif hasattr(self, name): 
            super().__setattr__(name, value)
        else:
            raise AttributeError("Local attributes are not allowed")

r = Rectangle(10, 20)
r.width = 15 
r.height = 25  
try:
    r.color = 'red'
except AttributeError as e:
    print(e)