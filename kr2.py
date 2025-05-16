print("Задача №1")
class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным числом")
        self._balance = value

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Депозит должен быть числом")
        if amount <= 0:
            raise ValueError("Депозит не может быть отрицательным числом")
        self._balance += amount
    
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Недостаточно средств на счете")
            elif amount <= 0:
                raise ValueError("Сумма снятия должна быть положительной")
            else:
                self.balance -= amount
        except Exception as e:
            print(f'Ошибка при снятии денег: {e}')

    def get_interest_rate(self):
        try:
            rate = 1000 / self.balance
            return f"Процентная ставка равна {rate:.2f}%"
        except ZeroDivisionError:
            return "Ошибка! Баланс равен нулю."

    def __str__(self):
        return f"Текущий баланс: {self.balance}"

account = BankAccount()
account.deposit(100)
print(account)
account.withdraw(33)
print(account)
print(account.get_interest_rate())

print("Задача №5")
class Product:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть текстовым значением")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена не может быть отрицательной и должна быть числом")
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

class Book(Product):
    def __init__(self, name, author, pages, price):
        super().__init__(name, price)
        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть текстовым значением")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("количество страниц не может быть отрицательной и должна быть числом")
        self._author = author
        self._pages = pages

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    def get_discounted_price(self, discount):
        if not isinstance(discount, (int, float)):
            raise TypeError("Скидка должна быть числом")
        if discount < 0:
            raise ValueError("Скидка не может быть отрицательной")
        try:
            return self._price * (1 - discount)
        except ZeroDivisionError:
            raise ZeroDivisionError("Ошибка, деление на 0")

    def __str__(self):
        return f"Книга: {self._name} Автор: {self._author}, {self._pages} страниц, цена: {self._price}"

class EBook(Book):
    def __init__(self, name, author, price, pages, file_size, file_format):
        super().__init__(name, author, price, pages)
        if not isinstance(file_size, (int, float)) or file_size <= 0:
            raise ValueError("Размер файла не может быть отрицательным")
        if not isinstance(file_format, str):
            raise TypeError("Файл должен быть текстом")
        self._file_size = file_size
        self._file_format = file_format
    
    @property
    def file_size(self, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Размер файла должен быть положительным числом")
        self._file_size = value
    
    @property
    def format(self, value):
        if not isinstance(value, str):
            raise TypeError("Формат должен быть строкой")
        self._format = value

    def __str__(self):
        return f"Электронная книга: {self._name}, Автор: {self._author}, {self._pages} страниц, цена: {self._price} размер: {self._file_size} Мбайт, расширение: {self._file_format}"


book = Book("Форма жизни №4", "Евгений Черешнев", 509, 778)
ebook = EBook("Форма жизни №4", "Евгений Черешнев",387, 499, 10.5, "PDF")
print(book)
print("Цена со скидкой:", book.get_discounted_price(0.1))
print(ebook)