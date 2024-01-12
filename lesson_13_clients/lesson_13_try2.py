import random
from abc import ABC, abstractmethod
from typing import Self


class Client:
    def __init__(self, name: str):
        self.name = name
        self.accounts: list['BaseAccount'] = []

    @property
    def positive_balance(self) -> bool:
        total_balance = sum([a.balance for a in self.accounts])
        balance_check = total_balance > 0
        return balance_check


class BaseAccount(ABC):
    def __init__(self):
        self.number = random.randint(21321454544, 999999999999999)
        self.balance = 0

    def deposit_money(self, summa):
        self.balance += summa

    @abstractmethod
    def make_transaction(self, other: Self, summa: int | float):
        pass

    def withdraw_money(self, summa: int | float):
        if self.balance - summa < 0:
            raise ValueError('Not enough money')
        self.balance -= summa


class CurrentAccount(BaseAccount):
    def make_transaction(self, other: BaseAccount, summa: int | float):
        if self.balance - summa < 0:
            print('Not enough money')
            return
        self.balance -= summa
        other.balance += summa


class CreditAccount(BaseAccount):
    percent_commission = 10 / 100

    def __init__(self, limit: int):
        super().__init__()
        self.limit = limit

    def make_transaction(self, other: BaseAccount, summa: int | float):
        if (self.balance - summa - (summa * self.percent_commission)) < self.limit:
            print('Not enough money')
            return
        self.balance -= summa + summa * self.percent_commission
        other.balance += summa
