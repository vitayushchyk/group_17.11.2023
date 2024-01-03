from typing import Self

import pytest

from lesson_13_clients.lesson_13_try2 import CurrentAccount, CreditAccount, Client, BaseAccount


class SimpleAccount(BaseAccount):
    """
    Fake class used to test BaseAccount functionality
    """

    def make_transaction(self, other: Self, summa: int | float):
        raise NotImplemented()


@pytest.fixture(scope='class')
def current_account() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope='class')
def credit_account() -> CreditAccount:
    instance = CreditAccount(limit=-2000)
    return instance


@pytest.fixture(scope='class')
def client() -> Client:
    instance = Client(name='Alex')
    return instance


@pytest.fixture(scope='class')
def another_client() -> Client:
    instance = Client(name='Bob')
    return instance


@pytest.fixture(scope='function')
def base_account() -> BaseAccount:
    instance = SimpleAccount()
    return instance
