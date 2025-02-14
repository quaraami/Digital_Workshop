print("Задание №1")
class Sauce:
    MAIN = "Майонез"
    def __init__(self, taste : str = None):
        self.taste = taste

    def show_my_sauce(self):
        if self.taste:
            print(f"Майонез и {self.taste}")
        else:
            print(str(Sauce.MAIN))
mayo_sauce = Sauce()
mayo_sauce.show_my_sauce()

cheese_sauce = Sauce("Сыр")
cheese_sauce.show_my_sauce()

garlic_sauce = Sauce("Чеснок")
garlic_sauce.show_my_sauce()


print("Задание №2")
class Employee:
    #@classmethod
    #def validate(cls, name, age, salary, bonus):
    #    return (
    #    isinstance(name, str) and
    #    isinstance(age, int) and 
    #    isinstance(salary, float) and
    #   isinstance(bonus, float)
    #    )
        
    def __init__(self, name, age, salary = 100000, bonus=0):
        #if self.validate(name, age, salary, bonus):
            self.name = name  
            self._age = age   
            self.__salary = salary  
            self.__bonus = 0 
        #else:
            #raise ValueError("Invalid input type")

    def get_name(self):
        return self.name
    def get_age(self):
        return self._age
    def get_salary(self):
        return self.__salary
    def set_bonus(self, bonus):
         self.__bonus = bonus
    def get_bonus(self):
        return self.__bonus
    def get_total_salary(self):
        return self.__salary + self.__bonus

Tim = Employee("Тимофей", 18)

print(f"Имя сотрудника: {Tim.get_name()}") 
print(f"Возраст сотрудника: {Tim.get_age()}")
print(f"Оклад сотрудника: {Tim.get_salary()}")
Tim.set_bonus(10000) #Установка бонуса
print(f"Общая зарплата сотрудника: {Tim.get_total_salary()}") #Вывод общей зарплаты


print("Задание №3")
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для '{self.name}':")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Сегодня мы готовим '{self.name}'.")
        print(f"Выполняем инструкцию по приготовлению блюда '{self.name}'...")
        print(f"Блюдо '{self.name}' готово!")
keks_recipe = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар"])
keks_recipe.print_ingredients()
keks_recipe.cook()
boloniese_recipe = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
boloniese_recipe.print_ingredients()
boloniese_recipe.cook()
