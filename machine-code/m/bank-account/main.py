"""
It's the bank system that appeared on the forum before,
just with slightly different methods at each level.

Level 1: createAccount, transfer

Level 2:
topNspender - requires sorting by pay and transfer amount.
If multiple accounts have the same ranking, sort alphabetically by account name

Level 3: payment - each transaction has 2% cashback that takes effect after 24 hours.
Required to return "payment" + a payment id, they gave examples like "payment1" etc.
This level also has another function, cancel

"""

from uuid import uuid4
from datetime import datetime

from sortedcontainers import SortedList


class Account:
    def __init__(self, account_num: int, account_name: str):
        self.timestamp_unix = datetime.now().timestamp()
        self.account_id = uuid4()
        self.account_name = account_name
        self.account_num = account_num
        self.withdraw = 0
        self.deposit = 0

    def get_balance(self):
        return self.deposit - self.withdraw

    def __str__(self):
        return f"""
        {self.account_name=}
        {self.timestamp_unix=}
        {self.account_id=}
        {self.get_balance()=}
        {self.withdraw=}
        {self.deposit=}
        """

    def __eq__(self):
        return self.account_id


class Transaction:
    def __init__(self, src_account_name: str, dest_account_name: str, amount: int):
        self.timestamp_unix = datetime.now().timestamp()
        self.src_account_name = src_account_name
        self.dest_account_name = dest_account_name
        self.amount = amount


class BankReport:
    def __init__(self):
        """Initialize the BankReport system."""
        self.accounts: dict[str, Account] = {}
        self.withdraw_indexed_acc: SortedList[tuple[float, str]] = SortedList()
        self.transactions = []

    # Level 1 Methods
    def createAccount(self, account_name: str):
        if account_name in self.accounts:
            return False
        account = Account(account_num=len(self.accounts), account_name=account_name)
        self.withdraw_indexed_acc.add((0, account.account_name))
        self.accounts[account.account_name] = account
        return True

    def transfer(self, src_account_name: str, dest_account_name: str, amount: float):
        src_account = self.accounts.get(src_account_name, False)
        if not src_account:
            print("Source account does not exist")
            return False
        dest_account = self.accounts.get(dest_account_name, False)
        if not src_account:
            print("Source account does not exist")
            return False
        self.transactions.append(Transaction(src_account_name, dest_account_name, amount))
        # Handle transaction logic - we will assume it is handled by DB
        self.withdraw_indexed_acc.discard((self.accounts[src_account_name].withdraw, src_account_name))
        self.accounts[src_account_name].withdraw -= amount
        self.accounts[dest_account_name].deposit += amount
        self.withdraw_indexed_acc.add((self.accounts[src_account_name].withdraw, src_account_name))
        print("modified the account:", src_account_name, self.accounts[src_account_name], amount)
        return True

    # Level 2 Method
    def topNspender(self, n):
        res = []
        # if withdraw is negative, we don't need to reverse for top n spend.
        # iterator = reversed(self.withdraw_indexed_acc)
        iterator = iter(self.withdraw_indexed_acc)
        sentinel = object()
        for i in range(n):
            elem = next(iterator, sentinel)
            if elem is sentinel:
                break
            res.append(elem[1])
        return res

    # Level 3 Methods
    def payment(self, timestamp, accountId, amount):
        """
        PAYMENTS [payment1 00:00 $10 | payment2 00:01 $50 | payment3 00:01 $50 ]
        CASHBACK_IS_PAID idx                                  i
        PAYMENTID {payment1: {idx: 0, canceled: False}, payment2: {idx: 1, canceled: False}}
        IF POINTER MOVED PAST, CANCEL, THEN UNDO CASHBACK ACCOUNT BALANCE PAYMT*CASHBK%
        IF WE CASHBACK, CASHBACK BALANCE on ACCOUNT += amount for that until we hit 24h timestamp and stop
        Monotonic queue with pointer and no deletions.
        """
        pass

    def cancel(self, timestamp, accountId, paymentId):
        pass


if __name__ == "__main__":
    CHAD = "chad"
    MARK = "mark"
    BOB = "bob"
    KILLA = "killa"
    bank_report = BankReport()
    bank_report.createAccount("chad")
    bank_report.createAccount("mark")
    bank_report.createAccount("bob")
    bank_report.createAccount("killa")
    for account_name in bank_report.accounts:
        print(bank_report.accounts[account_name])

    print("spend amounts--------------")
    bank_report.transfer(BOB, MARK, 400.23)
    bank_report.transfer(MARK, BOB, 22.44)
    bank_report.transfer(KILLA, BOB, 300.24)

    for account_name in bank_report.accounts:
        print(bank_report.accounts[account_name])

    print(bank_report.topNspender(3))
