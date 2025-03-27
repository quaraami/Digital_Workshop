print("Задание №1")
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    @staticmethod
    def check_positive_amount(amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        return True

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)

    def deposit(self, amount):
        self.check_positive_amount(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.check_positive_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счету.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Пример использования
if __name__ == "__main__":
    acc = BankAccount.create_empty_account("123456789")
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # Вывод: 300

print("Задание №2")
class User:
        def __init__(self, username, password=None):
            self.__username = username
            self.__password = None  # Пароль сначала пустой
            if password is not None and self.is_strong_password(password):
                self.__password = password
        @staticmethod
        def is_strong_password(password):
             return len(password) >= 6
        @classmethod
        def create_default_user(cls, username):
             default_password = f"{username}_strong_pass"
             return cls(username, default_password)
        def set_password(self, new_password):
            if self.is_strong_password(new_password):
                 self.__password = new_password
                 print("Пароль успешно изменён.")
            else:
                 print("Ошибка: пароль слишком короткий.")
        def get_username(self):
            return self.__username
# Пример использования
if __name__ == "__main__":
    user = User.create_default_user("Alice")
    print(user.get_username())  # Вывод: Alice
    user.set_password("12345")  # Ошибка: пароль слишком короткий
    user.set_password("securePass")  # Пароль успешно изменён

print("Задание №3")
import datetime

class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = self.validate_year(year)

    @staticmethod
    def validate_year(year):
        """Проверяет, что год издания корректный (int и не в будущем)."""
        current_year = datetime.datetime.now().year
        if isinstance(year, int) and year <= current_year:
            return year
        raise ValueError(f"Год {year} должен быть целым числом и не превышать текущий год ({current_year}).")

    @classmethod
    def create_default_year(cls, title, author):
        """Создает книгу с годом издания по умолчанию (2024)."""
        return cls(title, author, 2024)

    def get_info(self):
        """Возвращает информацию о книге в формате строки."""
        return f'"{self.__title}", автор: {self.__author}, год: {self.__year}'


# Пример использования
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"

    book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
    print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"