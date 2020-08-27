"""
This is the basic example of using pydantic BaseModels. Usage `python basic.py -v`
>>> saving_account_1 = SavingAccount(id='NASHVILLE-CUST-ABX100', account_holder='John Doe', amount=200.0, is_open=True)
>>> saving_account_1.deposit(25)
>>> saving_account_1.amount
225.0
>>> checking_account_1 = CheckingAccount(id='NASHVILLE-CUST-ABY100', account_holder='Jane Doe', amount=200.0, is_open=True, deposit_fee=2.0)
>>> checking_account_1.deposit(25)
>>> checking_account_1.amount
223.0
>>> checking_account_1.close()
"""

from abc import ABC, abstractmethod
from pydantic import BaseModel, Field


class Account(BaseModel, ABC):
    id: str = Field(
        ...,
        description="The id of the account"
    )

    account_holder: str = Field(
        ...,
        description="The name of the account holder"
    )

    amount: float = Field(
        ...,
        description="The amount in the account in dollars"
    )

    is_open: bool = Field(
        default=True,
        description="A flag indicating whether or not the account is open"
    )

    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError

    def close(self):
        self.is_open = False

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('Cannot withdraw to a closed account')

        if self.amount <= amount:
            self.amount -= amount
        else:
            raise ValueError('Cannot withdraw more than available funds.')

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'


class SavingAccount(Account):
    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('Cannot deposit to a closed account')

        self.amount += amount


class CheckingAccount(Account):
    deposit_fee: float = Field(
        default=0.0,
        description="Deposit fee for the checking account"
    )

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('Cannot deposit to a closed account')

        if amount < self.deposit_fee:
            raise ValueError('Amount is less than deposit fee')
        self.amount += (amount - self.deposit_fee)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
