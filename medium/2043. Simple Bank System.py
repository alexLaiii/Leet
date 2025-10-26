
"""
Simple Bank System (LeetCode 2043)

Stores balances for 1-indexed accounts and supports three O(1) operations:
  • deposit(account, money): add `money` to `account`
  • withdraw(account, money): subtract `money` from `account` if funds suffice
  • transfer(account1, account2, money): move `money` from `account1` to `account2`
    atomically (withdraw first; if deposit fails, roll back)

Contract:
  • Valid accounts are integers in [1, n].
  • Methods return True on success, False on failure.
  • State remains unchanged on failed operations (including failed transfers).

Complexity:
  • Time per operation: O(1)
  • Space: O(n) for balances

Parameters
----------
balance : List[int]
    Initial balances for n accounts; account i corresponds to index i-1.

Methods
-------
transfer(account1: int, account2: int, money: int) -> bool
    Withdraws from account1 and deposits into account2 atomically.
deposit(account: int, money: int) -> bool
    Deposits `money` into `account` if the account index is valid.
withdraw(account: int, money: int) -> bool
    Withdraws `money` from `account` if the account index is valid and balance is sufficient.
"""


class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance.copy()
        self.n = len(self.accounts)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            else:
                self.deposit(account1, money)
        return False
        
        

    def deposit(self, account: int, money: int) -> bool:
        if 1 > account or account > self.n:
            return False
        self.accounts[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if 1 > account or account  > self.n or self.accounts[account - 1] < money:
            return False
        self.accounts[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
