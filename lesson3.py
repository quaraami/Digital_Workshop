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