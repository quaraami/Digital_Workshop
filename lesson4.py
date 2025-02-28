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

print("Задание №2")