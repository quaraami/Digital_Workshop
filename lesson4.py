print("Задание №1")
class Person:
    def __init__(self, name, age):
            self.name = name  
            self.age = age
    def __setattr__(self, key, value):
        if key == 'name':
            if not isinstance(value, str) or len(value) == 0:
                raise ValueError("Name cannot be empty!")
        elif key == 'age':
            if not isinstance(value, (int)) or value <= 0:
                raise ValueError("Age must be a positive number!")
        super().__setattr__(key, value)

person = Person("John", 25)
print(f"Имя: { person.name}, Возраст: {person.age}")
p = Person("John", 25)  
p.name = "Alice"         
p.age = 30
print(f"Имя: { p.name}, Возраст: {p.age}")
p2 = Person("Timofey", 18)  
p2.name = ""              
p2.age = -5