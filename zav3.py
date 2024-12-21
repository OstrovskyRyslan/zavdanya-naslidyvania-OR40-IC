class BankAccount:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__balance = 0  
        self.__transaction_history = []
    def get_balance(self):
        return self.__balance
    def get_transaction_history(self):
        return self.__transaction_history
    def _record_transaction(self, amount):
        self.__transaction_history.append(amount)
class BaseCard(BankAccount):
    def __init__(self, user_id, card_id):
        super().__init__(user_id)
        self.__card_id = card_id
    def deposit(self, amount):
        self._record_transaction(f"Поповнено: {amount}")
        self._BankAccount__balance += amount
    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self._record_transaction(f"Знято: {amount}")
            self._BankAccount__balance -= amount
        else:
            print("Недостатньо коштів")
class SavingsCard(BaseCard):
    def __init__(self, user_id, card_id, interest_rate):
        super().__init__(user_id, card_id)
        self.__interest_rate = interest_rate
    def add_interest(self):
        interest = self.get_balance() * (self.__interest_rate / 100)
        self.deposit(interest)
        print(f"Додано відсотки: {interest}")
class PremiumCard(BaseCard):  
    def __init__(self, user_id, cashback_rate, card_id):
        super().__init__(user_id, card_id)
        self.__cashback_rate = cashback_rate
    def apply_cashback(self, amount):
        cashback = amount * (self.__cashback_rate / 100)
        self._BankAccount__balance += cashback
        self._record_transaction(f"Кешбек застосовано: {cashback}")
account = BaseCard(user_id=1, card_id="A1234")
account.deposit(100)
account.withdraw(50)
savings_account = SavingsCard(user_id=2, card_id="S5678", interest_rate=5)
savings_account.deposit(200)
savings_account.add_interest()
premium_account = PremiumCard(user_id=3, cashback_rate=2, card_id="P9876")
premium_account.deposit(300)
premium_account.apply_cashback(200)
print(f"Баланс BaseCard: {account.get_balance()}")
print(f"Історія транзакцій BaseCard: {account.get_transaction_history()}")
print(f"Баланс SavingsCard: {savings_account.get_balance()}")
print(f"Історія транзакцій SavingsCard: {savings_account.get_transaction_history()}")
print(f"Баланс PremiumCard: {premium_account.get_balance()}")
print(f"Історія транзакцій PremiumCard: {premium_account.get_transaction_history()}")
