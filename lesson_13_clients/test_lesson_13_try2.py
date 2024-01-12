import random

import pytest

from lesson_13_clients.lesson_13_try2 import CurrentAccount, CreditAccount, Client


class TestDepositFunds:
    def test_add_account_to_client(self, client, current_account):
        client.accounts.append(current_account)
        assert client.accounts

    def test_add_credit_account(self, client, credit_account):
        client.accounts.append(credit_account)
        assert len(client.accounts) == 2
        print(client.accounts)
        random.shuffle(client.accounts)

    def test_deposit_on_current_on_1560(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                account.deposit_money(1560)
                assert account.balance == 1560
                break

    def test_transfer_from_credit_to_debit(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                cur_acc = account
                break
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                cred_acc = account
                break

        cred_acc.make_transaction(cur_acc, 500)
        assert cur_acc.balance == 2060
        assert cred_acc.balance == (-500 - (500 * CreditAccount.percent_commission))

    def test_unsuccessful_from_current_account(self, current_account, credit_account):
        print(current_account.__dict__)
        balance_before = current_account.balance
        current_account.make_transaction(credit_account, 50000000000)
        assert current_account.balance == balance_before

    def test_withdraw_money_success(self, base_account):
        base_account.balance = 500

        base_account.withdraw_money(200)

        assert base_account.balance == 300

    def test_withdraw_money_error(self, base_account):
        base_account.balance = 100

        with pytest.raises(ValueError):
            base_account.withdraw_money(200)

    def test_adding_new_accounts(self, another_client):
        initial_len = len(another_client.accounts)
        another_client.accounts.extend([
            CreditAccount(100), CreditAccount(200),
            CurrentAccount(), CurrentAccount(),
        ])
        current_len = len(another_client.accounts)

        assert (initial_len + 4) == current_len

    def test_transfer(self):
        client_1 = Client(name='A')
        acc_1 = CreditAccount(-100)
        client_1.accounts = [acc_1]

        client_2 = Client(name='B')
        acc_2 = CreditAccount(-200)
        client_2.accounts = [acc_2]

        acc_1.make_transaction(acc_2, 1.33)

        assert client_1.accounts[0].balance == -1.463
        assert client_2.accounts[0].balance == 1.33
